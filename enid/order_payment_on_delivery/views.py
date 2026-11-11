from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from rest_framework.decorators import action
from order.serializer import OrderSerializer
from user.serializers.user_simple_validator import UserSimpleValidatorSerializer
from address.serializers.address_simple_validator_serializers import AddressSimpleValidatorSerializer
from .serializers import SourceValidatorSerializer
from order.models import Order
from address.models import Address
from products.models import Product
from item_order.models import ItemOrder
from django.contrib.auth.models import User
from state.models import State
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
from order.error_handling import ErrorResponse
import json
import hashlib

class OrderPaymentOnDeliveryViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=['post'], url_path='pod', url_name='pod')
    def create_order(self, request):
        data = request.data
        errors = self.validatorSerializers(data=data)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        # Validar fechas de entrega si algún producto las requiere
        date_errors = self._validate_delivery_dates(data)
        if date_errors:
            return Response(date_errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user, _ = self.register_user(data)
            address = self.register_address(data)
            products = data["products"]
            source = data.get('source', '')
            delivery_date = data.get('delivery_date')
            delivery_date_end = data.get('delivery_date_end')

            with transaction.atomic():
                order = self.create_order_instance(address, user, source, delivery_date, delivery_date_end)
                if isinstance(order, Order):
                    self.register_items_order(order, products)
                    serializer = OrderSerializer(order, context={'request': request})
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'No se pudo crear la orden.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(ErrorResponse.handle_exception(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _validate_delivery_dates(self, data):
        from products.models import Product as ProductModel
        products_data = data.get('products', [])

        requires_scheduling = False
        has_service = False

        for p_data in products_data:
            try:
                product = ProductModel.objects.get(id=p_data.get('id'))
                if product.allows_scheduled_delivery:
                    requires_scheduling = True
                    if product.is_service:
                        has_service = True
            except ProductModel.DoesNotExist:
                pass

        if not requires_scheduling:
            return None

        delivery_date = data.get('delivery_date')
        delivery_date_end = data.get('delivery_date_end')

        if not delivery_date:
            return {'delivery_date': 'Este campo es requerido para productos con agendamiento de entrega.'}

        if has_service and not delivery_date_end:
            return {'delivery_date_end': 'Este campo es requerido para servicios con rango de fechas.'}

        if has_service and delivery_date_end:
            from datetime import datetime
            try:
                start = datetime.strptime(delivery_date, '%Y-%m-%d').date()
                end = datetime.strptime(delivery_date_end, '%Y-%m-%d').date()
                if end < start:
                    return {'delivery_date_end': 'La fecha de fin debe ser mayor o igual a la fecha de inicio.'}
            except ValueError:
                return {'delivery_date': 'Formato de fecha inválido. Use YYYY-MM-DD.'}

        # Validate date format for single mode too
        if not has_service:
            from datetime import datetime
            try:
                datetime.strptime(delivery_date, '%Y-%m-%d')
            except ValueError:
                return {'delivery_date': 'Formato de fecha inválido. Use YYYY-MM-DD.'}

        return None

    @transaction.atomic
    def create_order_instance(self, address, user, source='', delivery_date=None, delivery_date_end=None):
        try:
            from datetime import datetime
            create_kwargs = {
                'shipping_address': address,
                'user': user,
                'payment_on_delivery': True
            }
            if source:
                create_kwargs['source'] = source
            if delivery_date:
                from django.utils import timezone
                naive_dt = datetime.strptime(delivery_date, '%Y-%m-%d')
                create_kwargs['delivery_date'] = timezone.make_aware(naive_dt)
            if delivery_date_end:
                create_kwargs['delivery_date_end'] = datetime.strptime(delivery_date_end, '%Y-%m-%d').date()

            return Order.objects.create(**create_kwargs)

        except IntegrityError as integrity_error:
            print(f"Error de integridad al crear la instancia de Order: {integrity_error}")
            return None
        except Exception as e:
            print(f"Error al crear la instancia de Order: {e}")
            return None


    def register_items_order(self, order, products):        
        try:
            for product in products:
                item = get_object_or_404(Product, id=product['id'], price=product['price'])
                if not Product.objects.filter(id=product['id'], price=product['price']).exists():
                    raise ValueError(f'El producto "{item}" no existe.')
                
                existing_item_order = ItemOrder.objects.filter(order=order, product=item).first()
                
                if existing_item_order:   
                    existing_item_order.quantity += product['quantity']
                    existing_item_order.save()
                
                else:

                    ItemOrder.objects.create(
                        order=order,
                        product=item,
                        quantity=product['quantity'],
                        price=product["price"])
                    
        except Exception as e:
            print(f"Error durante el registro de items en order: {type(e).__name__} - {str(e)}")
            raise  

    def register_user(self, data):
        """
        Registra o recupera un usuario.
        - Si viene 'email' en data (usuario autenticado), lo usa para buscar/crear el usuario
        - Si NO viene email (guest checkout), genera un email hash temporal
        """
        name = data.get('name', '')
        user_email = data.get('email', None)  # ✅ NUEVO: Obtener email del usuario autenticado
        
        # Si hay email del usuario autenticado, usarlo
        if user_email:
            print(f"🔗 Usuario autenticado detectado con email: {user_email}")
            defaults = {
                'username': user_email,
                'first_name': name.split()[0] if name else '',
                'last_name': ' '.join(name.split()[1:]) if name and len(name.split()) > 1 else ''
            }
            # Buscar o crear usuario con el email real
            user, created = User.objects.get_or_create(email=user_email, defaults=defaults)
            if created:
                print(f"✅ Nuevo usuario creado: {user_email}")
            else:
                print(f"✅ Usuario existente encontrado: {user_email}")
            return user, created
        
        # Si NO hay email (guest checkout), usar comportamiento legacy con hash
        else:
            print(f"📝 Guest checkout - generando email temporal para: {name}")
            name_hash = hashlib.sha1(name.encode('utf-8')).hexdigest()
            email = f"{name_hash[:10]}_{name.replace(' ', '').lower()}@gmail.com"
            defaults = {
                'username': email,
                'first_name': name.split()[0],
                'last_name': ' '.join(name.split()[1:])
            }
            # Create or get the user
            user, created = User.objects.get_or_create(email=email, defaults=defaults)
            return user, created


    def register_address(self, address_data):
        address = {
            "street": address_data['street'],
            "number": 1,
            "interior_number": 1,
            "state": State.objects.get(id=1),
            "phone_number": address_data['phone_number'],
        }
        
        return Address.objects.create(**address)
    

    def validatorSerializers(self, data):
        errors = {}        
        user_serializer = UserSimpleValidatorSerializer(data=data)
        if not user_serializer.is_valid():
            errors.update(user_serializer.errors)
            
        address_serializer = AddressSimpleValidatorSerializer(data=data)
        if not address_serializer.is_valid():
            errors.update(address_serializer.errors)

        # Validar el campo source
        source_serializer = SourceValidatorSerializer(data=data)
        if not source_serializer.is_valid():
            errors.update(source_serializer.errors)

        products = data.get("products", [])

        if not products:
            errors.update({"products": ["La orden debe tener al menos un producto."]})

        return errors
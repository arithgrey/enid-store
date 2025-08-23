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

        try:            
            user, _ = self.register_user(data)
            address = self.register_address(data)
            products = data["products"]
            source = data.get('source', '')  # Obtener el campo source

            with transaction.atomic():
                order = self.create_order_instance(address, user, source)  # Pasar source
                if isinstance(order, Order):
                    self.register_items_order(order, products)
                    serializer = OrderSerializer(order, context={'request': request})                                        
                    order_data = serializer.data                    
                    return Response(order_data, status=status.HTTP_201_CREATED)                    
                    
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        
     
        except Exception as e:            
            return Response(ErrorResponse.handle_exception(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    @transaction.atomic
    def create_order_instance(self, address, user, source=''):
        try:
            create_kwargs = {
                'shipping_address': address, 
                'user': user, 
                'payment_on_delivery': True
            }
            
            if source:
                create_kwargs['source'] = source
            
            order_instance = Order.objects.create(**create_kwargs)
            return order_instance
        
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
        
        name = data.get('name', '')
        name_hash = hashlib.sha1(name.encode('utf-8')).hexdigest()
        # solo para los casos donde es pay on delivery 
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
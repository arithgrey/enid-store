from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from rest_framework.decorators import action
from order.serializer import OrderSerializer
from user.serializers.user_validator_serializers import UserValidatorSerializer
from address.serializers.address_validator_serializers import AddressValidatorSerializer
from order.models import Order
from address.models import Address
from products.models import Product
from item_order.models import ItemOrder
from django.contrib.auth.models import User
from state.models import State
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from order.stripe_payment import StripePayment
from stripe.error import StripeError
from django.db import IntegrityError
from order.error_handling import ErrorResponse

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=['post'], url_path='compra')
    def create_order(self, request):
                
        data = request.data
        errors = self.validatorSerializers(data=data)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)    

        try:            
            user, _ = self.register_user(data)
            address = self.register_address(data)
            products = data["products"]

            with transaction.atomic():
                order = self.create_order_instance(address, user)
                if isinstance(order, Order):
                    self.register_items_order(order, products)
                    serializer = OrderSerializer(order, context={'request': request})                                        
                    stripe_payment = StripePayment()
                    charge_result = stripe_payment.stripeCharge(data=data, order=order)                    
                                        
                    if charge_result['status'] == 'success':                                        
                        return Response(serializer.data, status=status.HTTP_201_CREATED)                    
                    else:      
                        
                        transaction.set_rollback(True)
                        errors['stripe_error'] = charge_result['stripe_error']                                      
                        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

                    
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        
        except StripeError as e:                                 
            transaction.set_rollback(True)
            errors['stripe_error'] = charge_result['message']                                      
            return Response(errors,status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:            
            return Response(ErrorResponse.handle_exception(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


   

    @transaction.atomic
    def create_order_instance(self, address, user):
        try:
            order_instance = Order.objects.create(
                shipping_address=address, user=user)
            return order_instance
        
        except IntegrityError as integrity_error:            
            #print(f"Error de integridad al crear la instancia de Order: {integrity_error}")
            return None
        except Exception as e:
            
            ##print(f"Error al crear la instancia de Order: {e}")
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
            #print(f"Error durante el registro de items en order: {type(e).__name__} - {str(e)}")
            raise  

    def register_user(self, data):
        email = data['email']
        defaults = {
            'username': email,
            'first_name': data.get('name', '').split()[0],
            'last_name': ' '.join(data.get('name', '').split()[1:])
        }
        user, created = User.objects.get_or_create(email=email, defaults=defaults)
        return user, created


    def register_address(self, address_data):

        address = {
            "postal_code": address_data['postal_code'],
            "street": address_data['street'],
            "number": address_data['number'],
            "interior_number":address_data['number'],
            "colony": address_data['colony'],
            "delegation_or_municipality": address_data['delegation_or_municipality'],
            "city": address_data['city'],
            "state": State.objects.get(id=address_data["state"]),
            "phone_number": address_data['phone_number'],
        }
        
        return Address.objects.create(**address)
    

    def validatorSerializers(self, data):
        errors = {}
        
        if 'stripe_token' not in data:
            errors['stripe_token'] = ['El campo stripe_token es obligatorio.']

        user_serializer = UserValidatorSerializer(data=data)
        if not user_serializer.is_valid():
            errors.update(user_serializer.errors)

        address_serializer = AddressValidatorSerializer(data=data)
        if not address_serializer.is_valid():
            errors.update(address_serializer.errors)

        products = data.get("products", [])

        if not products:
            errors.update({"products": ["La orden debe tener al menos un producto."]})

        return errors
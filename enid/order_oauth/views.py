from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from rest_framework.decorators import action
from order.serializer import OrderSerializer
from address.serializers.address_validator_serializers import AddressValidatorSerializer
from order.models import Order
from rest_framework.exceptions import ValidationError
from order.stripe_payment import StripePayment
from stripe.error import StripeError
from order.error_handling import ErrorResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from order.views import OrderViewSet as OrderManager
from user.oauth_utils import AuthenticationChecker


class OrderViewSet(OrderManager, viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'], url_path='oauth', url_name='create_order')    
    def create_order(self, request):
                
        
        data = request.data
        errors = self.validatorSerializers(request=request,data=data)        
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)    

        user = request.user                
        
        try:            
            
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
                        order_data = serializer.data                        
                        return Response(order_data, status=status.HTTP_201_CREATED)     

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




    def validatorSerializers(self,request,data):

        authentication_error = AuthenticationChecker.check_authentication(request)
        if authentication_error:
            return authentication_error

        errors = {}
        
        if 'stripe_token' not in data:
            errors['stripe_token'] = ['El campo stripe_token es obligatorio.']      

        address_serializer = AddressValidatorSerializer(data=data)
        if not address_serializer.is_valid():
            errors.update(address_serializer.errors)

        products = data.get("products", [])

        if not products:
            errors.update({"products": ["La orden debe tener al menos un producto."]})

        return errors
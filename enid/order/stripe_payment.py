import stripe
from django.conf import settings
from rest_framework.response import Response
from order.error_handling import ErrorResponse

class StripePayment:
    
    def __init__(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY

    def stripeCharge(self, data, order):
               
        try:            
            total_amount = self._calculate_total(data['products'])
            metadata = self._prepare_metadata(order,data)

            charge = stripe.Charge.create(
                amount=int(total_amount * 100),  
                currency='mxn',
                source=data['stripe_token'],
                description=f'Order de compra {order.id}',
                metadata=metadata,
            )
            return self._handle_charge_response(charge)
        
        except stripe.error.CardError as e:                       
            return {'status': 'failed', 'stripe_error': e.user_message}
                    
        except stripe.error.StripeError as e:
            
            return {'status': 'failed', 'stripe_error': str(e)}
        
        except Exception as e:
            return {'status': 'failed'}
            
    
    def _calculate_total(self, products):            
        return sum(float(product['price']) * product['quantity'] for product in products)
    
    def _prepare_metadata(self, order, data):        
        return {
            'order_id': order.id,
            'email': data['email'] , 
            'phone_number': data['phone_number']
            }
    

    def _handle_charge_response(self, charge):
            
        if charge.status == 'succeeded':
            return {'status': 'success',
                    'message': f'Cargo exitoso. ID: {charge.id}'}
        else:
            return {
                'status': 'failed',
                'message': f'Cargo fallido. Estado: {charge.status}, Razón: {charge.failure_message}'}
                
        
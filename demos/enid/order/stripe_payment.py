import stripe
from django.conf import settings

class StripePayment:
    def stripeCharge(data, order):
        
        stripe.api_key = settings.STRIPE_SECRET_KEY        
        stripe_token  = data['stripe_token']
        products = data['products']
        total_amount = sum(float(product['price']) * product['quantity'] for product in products)        

        try:
            email = data['email']    
            phone_number = data['phone_number']

            metadata = {
                'order_id': order.id,
                'email': email, 
                'phone_number': phone_number
            }

            charge = stripe.Charge.create(
                amount=int(total_amount * 100),  
                currency='mxn',
                source=stripe_token,
                description=f'Order de compra {order.id}',
                metadata=metadata,
            )
            
            
            if charge.status == 'succeeded':
                response_data = {
                    'status': 'success',
                    'message': f'Cargo exitoso. ID: {charge.id}',
                }
            else:
                response_data = {
                    'status': 'failed',
                    'message': f'Cargo fallido. Estado: {charge.status}, Razón: {charge.failure_message}',
                }
                
            return response_data
        
        
        except stripe.error.CardError as e:        
            response_data = {
                'status': 'failed',
                'message': str(e),
            }
            return response_data

        except Exception as e:

            response_data = {
                'status': 'failed',
                'message': str(e),
            }
            return response_data            

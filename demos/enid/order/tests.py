from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from order.views import OrderViewSet
from user.serializers.user_validator_serializers import UserValidatorSerializer
from django.contrib.auth.models import User
from state.models import State

# Create your tests here.
class TestsOrderViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()   
        state = State.objects.create(name="CDMX")                
        self.required_fields = UserValidatorSerializer.Meta.required_fields
        self.not_allow_blank = UserValidatorSerializer.Meta.not_allow_blank
        self.max_lengths = UserValidatorSerializer.Meta.max_lengths
        self.min_lengths = UserValidatorSerializer.Meta.min_lengths
        self.max_values = UserValidatorSerializer.Meta.max_values
        self.min_values = UserValidatorSerializer.Meta.min_values

    
    def test_register_user(self):
        view = OrderViewSet()          
        data ={"user": {"email": "jmedrano@gmail9006.com","name": "Jonathan Govinda Medrano Salazar"}}
        user = view.register_user(data["user"])
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'jmedrano@gmail9006.com')
    
    def test_mark_error_on_invalid_data(self):
        
        invalid_data = {
            'user': {},
            'address': {},
            'products': []
        }
        response = self.client.post('/api/orden/compra/', invalid_data, format='json')                      
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_mark_error_on_required_fields(self):
        user_errors , address_errors = self.get_validator_errors()
        

    def get_validator_errors(self):
    
        invalid_data = {'user': {},'address':{}, "products":{}}
        response = self.client.post('/api/orden/compra/', invalid_data, format='json')
        
        user_errors = self.error_type(response, 'user')
        address_errors = self.error_type(response, 'address')        
                
        return user_errors , address_errors
    
    
    def error_type(self, response, key):
        
        field_errors = []
        if key in response.data:
            user_errors = response.data[key]
            for field, errors in user_errors.items():
                for error in errors:
                    code = getattr(error, 'code', None)
                    
                    error_info = {
                        'field': field,
                        'code': code if code else 'No disponible'
                    }
                    
                    field_errors.append(error_info)

        return field_errors
                               


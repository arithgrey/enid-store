from django.test import TestCase
from rest_framework.exceptions import ValidationError
from user.serializers.user_validator_serializers import UserValidatorSerializer
from faker import Faker
from share_test.tests import ValidatorTest

class UserValidatorSerializerTest(ValidatorTest):
    
    serializer_class = UserValidatorSerializer
    required_fields = UserValidatorSerializer.Meta.required_fields
    not_allow_blank = UserValidatorSerializer.Meta.not_allow_blank
    max_lengths = UserValidatorSerializer.Meta.max_lengths
    min_lengths = UserValidatorSerializer.Meta.min_lengths
    max_values = UserValidatorSerializer.Meta.max_values
    min_values = UserValidatorSerializer.Meta.min_values

    def setUp(self):                        
        self.fake = Faker('es_MX')    
        
    def test_invalid_email(self):

        data =  {'email': 'testexamp@´lecsom¿', 'name': self.fake.name()}
        serializer = self.serializer_class(data=data)            
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
    

    def test_valid_multiples_user(self):
        
        for _ in range(1000):
            user = {'email': self.fake.email(), 'name': self.fake.name()}        
            serializer = self.serializer_class(data=user)            
            if not serializer.is_valid():
                print(f"Error en user {user}: {serializer.errors}")

            self.assertTrue(serializer.is_valid())
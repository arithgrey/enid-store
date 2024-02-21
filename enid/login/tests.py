from django.test import TestCase
from unittest.mock import patch, Mock, call
from functools import reduce
from rest_framework.test import APIClient
from django.http import Http404
from rest_framework import status
from faker import Faker
from django.contrib.auth.models import User
from login.serializers import  UserSingInValidatorSerializer
from user.serializers.user_validator_serializers import UserValidatorSerializer
from share_test.tests import ValidatorTest
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

class TestUserSigin(ValidatorTest):
    serializer_class = UserSingInValidatorSerializer
    required_fields = UserSingInValidatorSerializer.Meta.required_fields
    not_allow_blank = UserSingInValidatorSerializer.Meta.not_allow_blank
    max_lengths =  {}
    min_lengths = {}
    min_values = {}
    max_values = {}

    def setUp(self):
        self.fake = Faker('es_MX')
        self.client = APIClient()        
        self.user = User.objects.create_user(
            username="arithgrey@gmail.com",
            email="arithgrey@gmail.com", 
            password="test_password_1",
            first_name="Jonathan")

    
    def test_sigin_with_empty_credentials(self):
        
        with patch('login.views.authenticate') as mock_authenticate:
        
            mock_authenticate.return_value = None
            data = {"email": "artihgrey@gmail.com", "password": "passss"}
            response = self.client.post('/api/login/sigin/', data=data, format='json')                
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_success_message_invalid_sinin(self):
        
        data = {"email":self.user.email,"password":"OTHER PASSWORD"}  
        response = self.client.post(
            '/api/login/sigin/', data, format='json')          
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        expected_error_message = "Credenciales inválidas"
        self.assertEqual(response.data['error'], expected_error_message)
        

    def test_success_sigin(self):

        group= Group.objects.create(name="ecommerce")
        self.user.groups.add(group)

        data = {"email":self.user.email,"password":"test_password_1"}  
        response = self.client.post(
            '/api/login/sigin/', data, format='json')  
                
        self.assertIn('token', response.data)
        self.assertEqual('ecommerce', response.data["profile"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        


class TestUserRegistration(ValidatorTest):
    serializer_class = UserValidatorSerializer
    required_fields = UserValidatorSerializer.Meta.required_fields
    not_allow_blank = UserValidatorSerializer.Meta.not_allow_blank
    max_lengths =  {}
    min_lengths = {}
    min_values = {}
    max_values = {}


    def setUp(self):
        self.fake = Faker('es_MX')
        self.client = APIClient()

    def faker_user(self):

        return {
            "email": self.fake.email(), 
            "name": self.fake.name(),
            "password": self.fake.password()
            }

    def test_success_singup(self):

        Group.objects.create(name="ecommerce")
        data = self.faker_user()
        response = self.client.post(
                '/api/login/signup/', data, format='json')  
        
        self.assertEqual(User.objects.count(),1)                
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_400_singup(self):
        
        data = {}
        response = self.client.post(
                '/api/login/signup/', data, format='json')  
                
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_400_password_singup(self):
        
        data = self.faker_user()
        data.pop("password")
        
        response = self.client.post(
            '/api/login/signup/', data, format='json')  
                
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_400_on_user_exists_singup(self):

        User.objects.create(username="Jonathan",email="arithgrey@gmail.com")
        
        data = {
            "email": "arithgrey@gmail.com",
            "name": self.fake.name(),
            "password": self.fake.password()
        }
        response = self.client.post('/api/login/signup/', data, format='json')          
        errors_email= response.data["email"]

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(errors_email[0], "Ya existe un usuario con este email.")
from django.test import TestCase
from unittest.mock import patch, Mock, call
from functools import reduce
from rest_framework.test import APIClient
from django.contrib.auth.models import User

# Create your tests here.
class TestsUserValidatorViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.email = "jmedrano@gmal.com"
    
    def tearDown(self):
        User.objects.all().delete()


    def test_handle_response_false_user_do_not_exists(self):
                
        response = self.client.get(
                f'/api/user/exists/{self.email}',  format='json')  
                
        self.assertEqual(response.status_code, 200)        
        expected_content = {"exists": False}
        self.assertEqual(response.json(), expected_content)


    def test_handle_response_true_when_user_exists(self):
                
        self.user = User.objects.create(email=self.email)
        response = self.client.get(
                f'/api/user/exists/{self.email}',  format='json')  
                
        self.assertEqual(response.status_code, 200)        
        expected_content = {"exists": True}
        self.assertEqual(response.json(), expected_content)    
        
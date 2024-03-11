from django.test import TestCase
from unittest.mock import patch, Mock, call
from functools import reduce
from rest_framework.test import APIClient
from django.http import Http404
from rest_framework import status
from order_oauth.views import OrderViewSet
from user.serializers.user_validator_serializers import UserValidatorSerializer
from address.serializers.address_validator_serializers import AddressValidatorSerializer
from faker import Faker
from django.contrib.auth.models import User
from state.models import State
from address.models import Address
from item_order.models import ItemOrder
from products.models import Product
import random
from order.models import Order
import re
from stripe.error import StripeError
from store.models import Store
from django.urls import reverse
from share_test.tests import ValidatorTest
from share_test.oauth import OAuthUtilities
from share_test.helpers.oauth_tests import OAuthTest
from share_test.mixin import CommonMixinTest

class OrderViewSetTest(CommonMixinTest):
    
    def setUp(self):
        super().setUp()                                      
        self.stripe_token = {'stripe_token':'stripe_token x'}
        self.api =  reverse("order_oauth-create_order")                
        self.oauthUtilities = OAuthUtilities()
        
            
    def test_create_valid_orders(self):        
        store = self.commons.create_fake_store()

        for _ in range(10):            
            address = self.commons.create_fake_address(create_object=False)   
                         
            products = {
                'products': self.commons.create_multiple_fake_products(
                quantity=3, as_dict=True, store=store)
                }

            data = {**address,**products, **self.stripe_token}            
            with patch('order.views.StripePayment.stripeCharge') as mock_stripe_charge:
                mock_response_data = {
                    'status': 'success',
                    'message': f'Cargo exitoso. ID: 17877',
                }

                mock_stripe_charge.return_value = mock_response_data
        
                _, api_oauth_client  = self.oauthUtilities.fake_user_and_api_client_with_headers(
                    store=store)

                response = api_oauth_client.post(self.api, data, format='json')                            
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        

class OrderViewSetRequireds(CommonMixinTest, ValidatorTest):
    '''Test to validate requireds, blanck, min, max lenghts on create order'''
    serializer_class = AddressValidatorSerializer

    def setUp(self):
        super().setUp()      
        self.required_fields = AddressValidatorSerializer.Meta.required_fields
        self.not_allow_blank = AddressValidatorSerializer.Meta.not_allow_blank
        self.max_lengths = AddressValidatorSerializer.Meta.max_lengths
        self.min_lengths = AddressValidatorSerializer.Meta.min_lengths
        self.min_lengths = AddressValidatorSerializer.Meta.min_lengths
        self.min_values = AddressValidatorSerializer.Meta.min_values
        self.max_values = AddressValidatorSerializer.Meta.max_values        
    
    
class AccessUserOrderCreate(OAuthTest):
    
    '''Test validate accesss on create order'''
    def setUp(self):             
        super().setUp()                                
        self.api = reverse("order_oauth-create_order")
        self.method ='post'                
        
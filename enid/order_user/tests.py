from django.test import TestCase
from share_test.mixin import CommonMixinTest
from django.urls import reverse
from order.models import Order
from rest_framework import status
from share_test.oauth import OAuthUtilities
from share_test.orders import OrderCreationServiceHelper
from share_test.helpers.oauth_tests import OAuthTest


class TestUserOrderFilter(TestCase):
    def setUp(self):            
        super().setUp()
        self.api = reverse('order_user:order-user')
        self.orderHelper = OrderCreationServiceHelper()
        self.oauthUtilities = OAuthUtilities()

    def test_filter_order_by_user(self):
                
        store = self.orderHelper.create_fake_store()
        user, api_oauth_client  = self.oauthUtilities.fake_user_and_api_client_with_headers(store=store)
                
        order = self.orderHelper.create_fake_order_with_products(
            user=user, store=store)        
        
        
        self.assertIsInstance(order, Order)
        order_id = order.id

        filters = {
            order.shipping_address.phone_number,                    
            order_id,
        }

        for item in filters:
            
            response = api_oauth_client.get(self.api, {"q":item})
            order_by_request = response.data[0]               
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data),1)            
            self.assertEqual(order_by_request["id"], order_id)


    def test_filter_order_by_total(self):
        
        store = self.orderHelper.create_fake_store()
        user, api_oauth_client  = self.oauthUtilities.fake_user_and_api_client_with_headers(store=store)
        _ = self.orderHelper.create_n_fake_orders(total_orders=4)
        fake_orders = self.orderHelper.create_n_fake_orders(
            user=user, store=store, total_orders=10)        
        
        
        self.assertEqual(len(fake_orders),10)
        response = api_oauth_client.get(self.api)        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),10)            

    
    def test_filter_order_by_status(self):
                
        store = self.orderHelper.create_fake_store()
        user, api_oauth_client  = self.oauthUtilities.fake_user_and_api_client_with_headers(
            store=store)
        
        fake_orders_shipped = self.orderHelper.create_n_fake_orders(
            user=user, store=store, total_orders=4, status='shipped')  
                
        
        response = api_oauth_client.get(self.api,{'status':fake_orders_shipped[0].status})        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),4)            
        


class TestsUserAccessOrder(OAuthTest):    
    '''Test validate accesss on order list'''
    def setUp(self):             
        super().setUp()                                
        self.api = reverse("order_user:order-user") 
        self.method  = 'get'

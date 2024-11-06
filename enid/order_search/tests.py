from django.test import TestCase
from share_test.mixin import CommonMixinTest
from django.urls import reverse
from order.models import Order
from rest_framework import status
from share_test.orders import OrderCreationServiceHelper
from share_test.oauth import OAuthUtilities

class TestsLeadSearchViewSet(CommonMixinTest,TestCase):
        
    def setUp(self):
        super().setUp()
        self.api = reverse('order_search:order-search')
        self.orderHelper = OrderCreationServiceHelper()
        self.oauthUtilities = OAuthUtilities()
        
        
    def test_filter(self):

        order = self.orderHelper.create_fake_order_with_products()                

        self.assertIsInstance(order, Order)    
                
        order_id = order.id
        filters = {
            order.shipping_address.phone_number,        
            order.user.username,
            order_id,
        }
        _, api_oauth_client  = self.oauthUtilities.fake_user_and_api_client()

        for item in filters:
            
            response = api_oauth_client.get(
                self.api, {"q":item})
            
            order_by_request = response.data[0]               
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data),1)            
            self.assertEqual(order_by_request["id"], order_id)
      

    def test_success_search_by_10_results(self):
       
       orders = self.orderHelper.create_n_fake_orders(total_orders=10)       
       self.assertEqual(len(orders),10)

       _, api_oauth_client  = self.oauthUtilities.fake_user_and_api_client()
       response = api_oauth_client.get(self.api, {})       
       self.assertEquals(len(response.data),10)
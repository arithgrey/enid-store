from django.test import TestCase
from share_test.mixin import CommonMixinTest
from django.urls import reverse
from order.models import Order
from rest_framework import status
from store.models import Store
from share_test.orders import OrderCreationHelper

class TestsLeadSearchViewSet(CommonMixinTest,TestCase):
        
    def setUp(self):
        super().setUp()
        self.api = reverse('order_search:order-search')
        self.orderHelper = OrderCreationHelper()
        
        
    def test_success_on_requireds_400(self):
            
        response = self.client.get(self.api, {},format='json')        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    
    def test_filter(self):

        order = self.orderHelper.create_fake_order_with_products()                
        store = order.store

        self.assertIsInstance(order, Order)    
        self.assertIsInstance(store, Store)                
        headers = self.commons.add_headers_store(store)
        
        order_id = order.id
        filters = {
            order.shipping_address.phone_number,        
            order.user.username,
            order_id,
        }

        for item in filters:
            
            response = self.client.get(
                self.api, {"q":item}, format='json', **headers)

            order_by_request = response.data[0]               
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data),1)            
            self.assertEqual(order_by_request["id"], order_id)
            

    def test_success_search_by_10_results(self):
       
       store = self.commons.create_fake_store() 
       orders = [self.orderHelper.create_fake_order_with_products(store=store) for _ in range(10)]
       self.assertEqual(len(orders),10)

       headers = self.commons.add_headers_store(store=store)
       response = self.client.get(self.api, {}, format='json', **headers)
       
       self.assertEquals(len(response.data),10)


    def test_associated_(self):
       
       store = self.commons.create_fake_store() 
       orders = [self.orderHelper.create_fake_order_with_products(store=store) for _ in range(10)]
       self.assertEqual(len(orders),10)

       headers = self.commons.add_headers_store(store=store)
       response = self.client.get(self.api, {}, format='json', **headers)
       
       self.assertEquals(len(response.data),10)
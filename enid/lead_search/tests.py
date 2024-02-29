from django.test import TestCase
from share_test.mixin import CommonMixinTest
from django.urls import reverse
from store.models import Store
from rest_framework import status

class TestsLeadSearchViewSet(CommonMixinTest,TestCase):
        
    def setUp(self):
        super().setUp()
        self.api = reverse('lead_search:lead-search')

    def add_headers_store(self, store):

        if isinstance(store, Store):
            store_id = store.id
            return {'HTTP_X_STORE_ID': store_id}
        
    def test_success_on_requireds_400(self):
            
        response = self.client.get(self.api, {},format='json')        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_success_search_by_email(self):

        email="jmedrano@9006.com"
        lead = self.commons.create_fake_lead(email=email)        
        headers = self.add_headers_store(lead.store)

        response = self.client.get(
            self.api, {"q":email, 'status':'pending'},
            format='json',  
            **headers
            )        
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
       

    def test_success_search_by_name(self):

        name="jonathan Medrano"
        lead = self.commons.create_fake_lead(name=name)        
        headers = self.add_headers_store(lead.store)

        response = self.client.get(
            self.api, {"q":name, 'status':'pending'},
            format='json',  
            **headers
            )        
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    
    def test_success_search_by_phone_number(self):

        phone_number="5552967027"
        lead = self.commons.create_fake_lead(phone_number=phone_number)        
        headers = self.add_headers_store(lead.store)

        response = self.client.get(
            self.api, {"q":phone_number, 'status':'pending'},
            format='json',  
            **headers
            )        
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
          

    def test_success_search_by_10_results(self):    

        store = self.commons.create_fake_store()
        for _ in range(10):
            lead = self.commons.create_fake_lead(store=store)
        
    
        headers = self.add_headers_store(lead.store)

        response = self.client.get(
            self.api, {'status':'pending'},
            format='json',  
            **headers
            )        
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertEqual(len(response.data), 10)


    def test_by_status(self):

        discarded_lead = self.commons.create_fake_lead(status='discarded')    
        headers = self.add_headers_store(discarded_lead.store)
        response = self.client.get(
            self.api, {'status':'discarded'},
            format='json',  
            **headers
            )                
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertEqual(len(response.data), 1)
         

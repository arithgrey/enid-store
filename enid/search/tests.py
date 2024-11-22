from django.test import TestCase
from rest_framework.test import APIClient
from django.http import Http404
from rest_framework import status
from faker import Faker
from products.models import Product
from share_test.commons import CommonsTest
from django.urls import reverse


class TestProductSeachByQViewSet(TestCase):
 
    def setUp(self):
        self.fake = Faker('es_MX')
        self.client = APIClient()
        self.commons = CommonsTest()
            

    # def test_find_produc_by_name(self):
        
    #     q='pesas'   
    #     product = self.commons.create_fake_product(name=q)
    #     if isinstance(product,Product):            
            
    #         url = reverse('get_by_q', kwargs={'q': q})            
    #         response = self.client.get(url, format='json')            

    #         response_product = response.data["results"]
    #         self.assertEqual(response.status_code, status.HTTP_200_OK)
    #         self.assertEqual(len(response_product),1)    
    #         self.assertEqual(response_product[0]['name'], product.name)
    
    
    # def test_find_produc_category_name(self):
    #     q='deportivos'
    #     product = self.commons.create_fake_product(name=q)
    #     if isinstance(product,Product):                        
                        
    #         url = reverse('get_by_q', kwargs={'q': q})
            
    #         response = self.client.get(url, format='json')                        
    #         category_product_name = product.category.name                                    
            
    #         response_product = response.data["results"]                        
    #         self.assertEqual(response.status_code, status.HTTP_200_OK)
    #         self.assertEqual(len(response_product),1)                
    #         self.assertEqual(response_product[0]['category']['name'], category_product_name)            

              
    # def test_return_404_on_q_missing(self):
        
    #     response = self.client.get('/api/search/product/', format='json')                                      
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        

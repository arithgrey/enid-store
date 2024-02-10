from django.test import TestCase
from rest_framework.test import APIClient
from django.http import Http404
from rest_framework import status
from faker import Faker
from products.models import Product
from categories.models import Category

class TestProductSeachByQViewSet(TestCase):
 
    def setUp(self):
        self.fake = Faker('es_MX')
        self.client = APIClient()
        
    def create_fake_product(self):
        category = Category.objects.create(name="equipos deportivos")
        product = Product.objects.create(
            name="Producto que tiene la palabra pesas en algun momento",
            category=category,
            price=2100
            )
        return product
        

    def test_find_produc_by_name(self):
        
        product = self.create_fake_product()
        if isinstance(product,Product):            
            q='pesas'   
            response = self.client.get(
                    f'/api/search/product/{q}/', format='json')              
                        
            response_product = response.data["results"]
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response_product),1)    
            self.assertEqual(response_product[0]['name'], product.name)
    
    def test_find_produc_category(self):
        
        product = self.create_fake_product()        
        if isinstance(product,Product):                        
            q='deportivos'            
            response = self.client.get(
                    f'/api/search/product/{q}/', format='json')  
                        
            category_product_name = product.category.name                        
            
            response_product = response.data["results"]
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response_product),1)                
            self.assertEqual(response_product[0]['category']['name'], category_product_name)            

              
    def test_return_404_on_q_missing(self):
        
        response = self.client.get('/api/search/product/', format='json')                                      
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        

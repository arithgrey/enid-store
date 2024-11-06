from faker import Faker
from unittest.mock import patch, Mock, call
from products.models import Product
from categories.models import Category
from state.models import State
from address.models import Address
from django.contrib.auth.models import User
import re 
import random

class CommonsTest:

    def __init__(self):
        self.fake = Faker('es_MX')

    def create_fake_category(self):

        return Category.objects.create(name=self.fake.word())


    def create_fake_product(self, **kwargs):
    
        defaults = {
            'name': self.fake.word(),
            'price': self.fake.random_int(min=100, max=10000)
        }
        
        params = {**defaults, **kwargs}
        
        if 'category' not in params:
            
            params['category'] = self.create_fake_category()

        product = Product.objects.create(**params)
        
        return product
    


    def create_multiple_fake_products(self, quantity=1, as_dict=False, **kwargs):
        products = []
        for _ in range(quantity):
            product = self.create_fake_product(**kwargs)
            if as_dict:
                product_dict = {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'quantity': random.randint(1, 100)
                }
                products.append(product_dict)
            else:
                products.append(product)
        return products
    
    
    def create_fake_state(self, **kwargs):
        
        defaults = {            
            "name": self.fake.name(),            
        }

        params = {**defaults, **kwargs}      

        return State.objects.create(**params)
        

    def create_fake_address(self, create_object=True, **kwargs):

        postal_code = self.fake.postcode()
        street = self.fake.street_address()
        number = self.fake.random_int(min=1, max=10000)
        interior_number = self.fake.random_int(min=1, max=9999)          
        colony = self.fake.city_prefix()
        delegation_or_municipality = self.fake.city()
        city = self.fake.city()        
        phone_number = self.fake.phone_number().split('x')[0].strip()
        cleaned_phone_number = re.sub(r'[^0-9]', '', phone_number)

        defaults = {
            "postal_code": postal_code,
            "street": street,
            "number": number,
            "interior_number":interior_number,
            "colony": colony,
            "delegation_or_municipality": delegation_or_municipality,
            "city": city,
            "state": self.create_fake_state(),
            "phone_number": cleaned_phone_number,
        }
        
        params = {**defaults, **kwargs}      

        if create_object:
            return Address.objects.create(**params)
        else:            
            params["state"] = params["state"].id
            return params


    def crear_fake_user(self, **kwargs):
        
        email = self.fake.email()
        name= self.fake.name()

        defaults = {
            'username': email,
            'first_name': name,
            'last_name': self.fake.last_name()
        }
        params = {**defaults, **kwargs}      
        return User.objects.create(**params)
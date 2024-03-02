from faker import Faker
from unittest.mock import patch, Mock, call
from products.models import Product
from categories.models import Category
from store.models import Store
from lead.models import Lead
from lead_type.models import LeadType
from state.models import State
from address.models import Address
from django.contrib.auth.models import User
from item_order.models import ItemOrder
from order.models import Order
import re 
import random

class CommonsTest:

    def __init__(self):
        self.fake = Faker('es_MX')
    
    def create_fake_lead(self, **kwargs):
        store = self.create_fake_store()
        
        defaults = {
            "email": self.fake.email(), 
            "name": self.fake.name(),
            "phone_number": self.fake.phone_number().split('x')[0].strip(),
            "lead_type": LeadType.objects.create(name="En intento de compra"),
            "store":store
        }

        params = {**defaults, **kwargs}       
        return Lead.objects.create(**params)
    
            

    def create_fake_category(self, store = None):

        if not isinstance(store, Store):
            store = Store.objects.create(name=self.fake.company())

        return Category.objects.create(name=self.fake.word(), store=store)


    def create_fake_product(self, **kwargs):
        

        defaults = {
            'name': self.fake.word(),
            'price': self.fake.random_int(min=100, max=10000)
        }
        
        params = {**defaults, **kwargs}

        if 'category' not in params:
            store = Store.objects.create(name=self.fake.company())
            params['store'] = store
            params['category'] = self.create_fake_category(store)

        product = Product.objects.create(**params)
        
        return product
    
    def create_fake_store(self, **kwargs):
        
        defaults = {
            'name': self.fake.word(),            
        }
        
        params = {**defaults, **kwargs}
        store = Store.objects.create(**params)
        
        return store
    

    def add_headers_store(self, store):

        if isinstance(store, Store):
            store_id = store.id
            return {'HTTP_X_STORE_ID': store_id}
        
    
    def create_fake_state(self, **kwargs):
        
        defaults = {            
            "name": self.fake.name(),            
        }

        params = {**defaults, **kwargs}      

        return State.objects.create(**params)
        

    def create_fake_address(self, **kwargs):

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

        return Address.objects.create(**params)
    

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
            
        
    def create_fake_order_with_products(self, store=None, num_products=3, **kwargs):
        
        if store is None:
            store = self.create_fake_store()

        address = self.create_fake_address()
        user = self.crear_fake_user()
    
        if 'store' not in kwargs:
            kwargs['store'] = store

        order = Order.objects.create(user=user, shipping_address=address, **kwargs)
        products = [self.create_fake_product(store=store) for _ in range(num_products)]

        for product in products:
            quantity = random.randint(1, 10)
            price = product.price
            ItemOrder.objects.create(
                order=order, product=product, quantity=quantity, price=price)

        return order
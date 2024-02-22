from django.test import TestCase
from unittest.mock import patch, Mock, call
from functools import reduce
from rest_framework.test import APIClient
from django.http import Http404
from rest_framework import status
from categories.models import Category
from order.views import OrderViewSet
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



class LeadViewSet(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='jonathan')
        self.fake = Faker('es_MX')
        self.client = APIClient()
        self.view = OrderViewSet()
        self.state = State.objects.create(name="CDMX")
        self.category = Category.objects.create(name="test category")
        self.required_fields = UserValidatorSerializer.Meta.required_fields
        self.not_allow_blank = UserValidatorSerializer.Meta.not_allow_blank
        self.max_lengths = UserValidatorSerializer.Meta.max_lengths
        self.min_lengths = UserValidatorSerializer.Meta.min_lengths
        self.max_values = UserValidatorSerializer.Meta.max_values
        self.min_values = UserValidatorSerializer.Meta.min_values

        self.required_fields_address = AddressValidatorSerializer.Meta.required_fields
        self.not_allow_blank_address = AddressValidatorSerializer.Meta.not_allow_blank
        self.max_lengths_address = AddressValidatorSerializer.Meta.max_lengths
        self.min_lengths_address = AddressValidatorSerializer.Meta.min_lengths
        self.min_lengths_address = AddressValidatorSerializer.Meta.min_lengths
        self.min_values_address = AddressValidatorSerializer.Meta.min_values
        self.max_values_address = AddressValidatorSerializer.Meta.max_values
        self.stripe_token = {'stripe_token':'stripe_token x'}


    def test_mark_error_on_required_stripe_token(self):

        invalid_data = {}
        errors = self.make_the_type_of_error(invalid_data)            
        has_stripe_token = self.has_stripe_token_error(errors)                 
        self.assertTrue(has_stripe_token,'ok test pass on required stripe_token')

    
    def test_handle_stripe_failed_payment(self):       
                 
        with patch('order.views.StripePayment.stripeCharge') as mock_stripe_charge:
            
            mock_response_data = {
                'status': 'Failed',
                'stripe_error': f'Falla en el cargo',
            }
            mock_stripe_charge.return_value = mock_response_data
            user = {"email": self.fake.email(), "name": self.fake.name()}
            address = self.create_fake_address(False)
            products = {'products':self.create_fake_products(random.randint(1,10))}            
            data = {**user, **address,**products, **self.stripe_token}            
            
            response = self.client.post(
                '/api/orden/compra/', data, format='json')  
                        
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_handle_stripe_success_payment(self):       
                 
        with patch('order.views.StripePayment.stripeCharge') as mock_stripe_charge:
            
            mock_response_data = {
                'status': 'success',
                'message': f'Cargo exitoso. ID: 17877',
            }
            mock_stripe_charge.return_value = mock_response_data
            user = {"email": self.fake.email(), "name": self.fake.name()}
            address = self.create_fake_address(False)
            products = {'products':self.create_fake_products(random.randint(1,10))}
            stripe_token = {'stripe_token':'stripe_token x'}
            data = {**user, **address,**products, **stripe_token}            
            
            response = self.client.post(
                '/api/orden/compra/', data, format='json')  
                        
            self.assertEqual(Order.objects.count(), 1)              
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_valid_orders(self):

        for _ in range(0):

            user = {"email": self.fake.email(), "name": self.fake.name()}
            address = self.create_fake_address(False)
            products = {'products':self.create_fake_products(random.randint(1,10))}
            data = {**user, **address,**products, **self.stripe_token}            
            with patch('order.views.StripePayment.stripeCharge') as mock_stripe_charge:
                mock_response_data = {
                    'status': 'success',
                    'message': f'Cargo exitoso. ID: 17877',
                }

                mock_stripe_charge.return_value = mock_response_data
                response = self.client.post(
                    '/api/orden/compra/', data, format='json')  
                
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_error_on_create_valid_orders_without_products(self):
        for _ in range(1):

            user = {"email": self.fake.email(), "name": self.fake.name()}
            address = self.create_fake_address(False)
            products = {'products':[]}
            data = {**user, **address,**products}            
            
            response = self.client.post(
                '/api/orden/compra/', data, format='json')            
                                         
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                  

    def create_fake_address(self, create_object=True):

        postal_code = self.fake.postcode()
        street = self.fake.street_address()
        number = self.fake.random_int(min=1, max=10000)
        interior_number = self.fake.random_int(min=1, max=9999)          
        colony = self.fake.city_prefix()
        delegation_or_municipality = self.fake.city()
        city = self.fake.city()
        id = self.state.id
        phone_number = self.fake.phone_number().split('x')[0].strip()
        cleaned_phone_number = re.sub(r'[^0-9]', '', phone_number)

        address_data = {
            "postal_code": postal_code,
            "street": street,
            "number": number,
            "interior_number":interior_number,
            "colony": colony,
            "delegation_or_municipality": delegation_or_municipality,
            "city": city,
            "state": id,
            "phone_number": cleaned_phone_number,
        }

        if create_object:
            return self.view.register_address(address_data=address_data)

        return address_data

    def create_fake_products(self, items):

        products = []
        for _ in range(items):

            product_name = self.fake.word()
            price = round(random.uniform(1.0, 1000.0), 2)
            product, created = Product.objects.get_or_create(
                name=product_name,
                price=price,
                category=self.category
            )

            product_dict = {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'quantity': random.randint(1, 100)
            }

            products.append(product_dict)
        return products

    def test_register_address(self):

        for _ in range(100):
            address = self.create_fake_address()
            self.assertIsInstance(address, Address)

    def test_register_user(self):

        for _ in range(100):

            email = self.fake.email()
            data = {"email": email, "name": self.fake.name()}
            user, _ = self.view.register_user(data)
            self.assertIsInstance(user, User)
            self.assertEqual(user.email, email)

    def test_mark_error_on_invalid_data(self):

        invalid_data = {}
        response = self.client.post(
            '/api/orden/compra/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_mark_error_when_minor_the_min_value_user(self):

        user_min_values = self.min_values
        invalid_data = {key: (value - 1)
                        for key, value in user_min_values.items()}

        self.generic_errors(invalid_data=invalid_data,
                            rules_expecteds=user_min_values, rule='min_value')

    def test_mark_error_when_minor_the_min_value_address(self):

        address_min_values = self.min_values_address
        

        invalid_data = {key: (value - 1)
                        for key, value in address_min_values.items()}

        self.generic_errors(invalid_data=invalid_data,
                            rules_expecteds=address_min_values, rule='min_value')

    def test_mark_error_when_pass_the_max_value_address(self):

        address_max_values = self.max_values_address

        invalid_data = {key: (value + 1)
                        for key, value in address_max_values.items()}

        self.generic_errors(invalid_data=invalid_data,
                            rules_expecteds=address_max_values, rule='max_value')

    def test_mark_error_when_pass_the_max_value_user(self):

        users_max_values = self.max_values

        invalid_data = {key: (value + 1)
                        for key, value in users_max_values.items()}

        self.generic_errors(invalid_data=invalid_data,
                            rules_expecteds=users_max_values, rule='max_value')

    def test_return_error_when_input_is_minor_of_the_rules_minlength_address(self):

        min_lengths = self.min_lengths_address
        invalid_data = {key: 'a' * (value - 1)
                        for key, value in min_lengths.items()}

        self.generic_errors(invalid_data=invalid_data,
                            rules_expecteds=min_lengths, rule='min_length')

    def test_return_error_when_input_is_minor_of_the_rules_minlength_user(self):

        users_min_lengths = self.min_lengths

        invalid_data = {key: 'a' * (value - 1)
                        for key, value in users_min_lengths.items()}

        self.generic_errors(invalid_data=invalid_data,
                            rules_expecteds=users_min_lengths, rule='min_length')

    def test_mark_error_when_pass_the_max_length_user(self):

        user_max_lengths = self.max_lengths

        invalid_data = {key: 'a' * (value + 1)
                        for key, value in self.max_lengths.items()}

        self.generic_errors(invalid_data=invalid_data,
                            rules_expecteds=user_max_lengths, rule='max_length')

    def test_mark_error_when_pass_the_max_length_address(self):

        max_lengths = self.max_lengths_address
        invalid_data = {key: 'a' * (value + 1)
                        for key, value in max_lengths.items()}

        self.generic_errors(invalid_data=invalid_data,
                            rules_expecteds=max_lengths, rule='max_length')

    def test_mark_error_on_user_blank_fields(self):

        invalid_data = {key: '' for key in self.not_allow_blank}
        self.blanks_asserts(invalid_data=invalid_data, rules_expecteds=self.not_allow_blank)

    def test_mark_error_on_address_blank_fields(self):

        invalid_data = {key: '' for key in self.not_allow_blank_address}
        self.blanks_asserts(invalid_data=invalid_data, rules_expecteds=self.not_allow_blank_address)
        

    def has_stripe_token_error(self, errors):
        return any(error.get('field') == 'stripe_token' for error in errors)
            
        
    def test_mark_error_on_user_required_fields(self):

        invalid_data = {}
        user_errors = self.make_the_type_of_error(invalid_data)
        required_user_fields = self.required_fields
        filtered_user_errors = list(
            filter(lambda error: error['field'] in required_user_fields, user_errors))
        user_errors_api = [item['field'] for item in filtered_user_errors]
        self.assertEqual(required_user_fields, user_errors_api,
                         "Las listas no son iguales.")

    def test_mark_error_on_address_required_fields(self):

        invalid_data = {}
        address_errors = self.make_the_type_of_error(invalid_data)

        required_address_fields = self.required_fields_address
        filtered_address_errors = list(
            filter(lambda error: error['field'] in required_address_fields, address_errors))
        address_errors_api = [item['field']
                              for item in filtered_address_errors]
        self.assertEqual(required_address_fields,
                         address_errors_api, "Las listas no son iguales.")

    def make_the_type_of_error(self, invalid_data):

        response = self.client.post(
            '/api/orden/compra/', invalid_data, format='json')
        return self.error_type(response)

    def filter_errors(self, code, requireds, errors):

        filtered_errors = list(filter(
            lambda error: error['field'] in requireds and error['code'] == code, errors))
        return [item['field'] for item in filtered_errors]

    def error_type(self, response):

        field_errors = []
        user_errors = response.data
        for field, errors in user_errors.items():
            for error in errors:
                code = getattr(error, 'code', None)

                error_info = {
                    'field': field,
                    'code': code if code else 'No disponible'
                }

                field_errors.append(error_info)

        return field_errors
    

    def create_fake_order(self):
        email = self.fake.email()
        data = {"email": email, "name": self.fake.name()}
        user, _ = self.view.register_user(data)
        address = self.create_fake_address()
        return self.view.create_order_instance(address=address,user=user)


    def test_create_order_instance(self):
        order_instance = self.create_fake_order()
        self.assertIsInstance(order_instance, Order)
            

    def test_register_items_order_success(self):     

        with patch('order.views.get_object_or_404') as mock_get_object:
            
            mock_product = Product(id=1, name='Example Product', price=10.0)
            mock_get_object.return_value = mock_product

            order = self.create_fake_order()
            expected_products = self.create_fake_products(5)

            total_quantity_expected = reduce(lambda acc, product: acc + product["quantity"], expected_products,0)
            

            self.view.register_items_order(order=order, products=expected_products)   
            
            expected_calls = [call(Product, id=product['id'], price=product['price']) for product in expected_products]
            mock_get_object.assert_has_calls(expected_calls, any_order=True)         
            item_orders = ItemOrder.objects.filter(order=order)            
            total_quantity = reduce(lambda acc, item_order: acc + item_order.quantity, item_orders, 0)
                    
            self.assertEqual(total_quantity_expected, total_quantity)

    
    def test_register_items_order_failure_product_not_found(self):
        
        order = Order.objects.create()
        expected_products = [
            {'id': 1, 'price': 10.0, 'quantity': 2},
            {'id': 2, 'price': 20.0, 'quantity': 3}
        ]
        
        with patch('order.views.get_object_or_404') as mock_get_object:
            # Configura el retorno del mock para simular un producto no encontrado
            mock_get_object.side_effect = Http404("Product not found")
            
            with self.assertRaises(Http404):
                self.view.register_items_order(order=order, products=expected_products)
            
            mock_get_object.assert_called_with(Product, id=1, price=10.0)

            item_orders = ItemOrder.objects.filter(order=order)
            self.assertEqual(len(item_orders), 0)
    
   
    def blanks_asserts(self, invalid_data,rules_expecteds):

        user_errors = self.make_the_type_of_error(invalid_data)
        user_errors_api = self.filter_errors('blank', rules_expecteds, user_errors)
        self.assertEqual(rules_expecteds, user_errors_api, "Las listas no son iguales.")
        
    def generic_errors(self, invalid_data, rules_expecteds, rule):

        user_errors = self.make_the_type_of_error(invalid_data)
        user_errors_api = self.filter_errors(
            rule, rules_expecteds, user_errors)        
        keys = list(rules_expecteds.keys())
        self.assertCountEqual(keys, user_errors_api, "Las listas no son iguales.")

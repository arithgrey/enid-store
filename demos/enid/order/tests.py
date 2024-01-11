from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from order.views import OrderViewSet
from user.serializers.user_validator_serializers import UserValidatorSerializer
from address.serializers.address_validator_serializers import AddressValidatorSerializer

from django.contrib.auth.models import User
from state.models import State


class TestsOrderViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()
        state = State.objects.create(name="CDMX")
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

    def test_register_user(self):
        view = OrderViewSet()
        data = {"user": {"email": "jmedrano@gmail9006.com",
                         "name": "Jonathan Govinda Medrano Salazar"}}
        user = view.register_user(data["user"])
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'jmedrano@gmail9006.com')

    def test_mark_error_on_invalid_data(self):

        invalid_data = {
            'user': {},
            'address': {},
            'products': []
        }
        response = self.client.post(
            '/api/orden/compra/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_mark_error_when_minor_the_min_value_user(self):

        user_min_values = self.min_values

        invalid_data = {
            'user': {key: (value - 1) for key, value in user_min_values.items()}}
        user_errors = self.make_the_type_of_error(invalid_data, 'user')
        user_errors_api = self.filter_errors(
            'min_value', user_min_values, user_errors)
        
        keys = list(user_min_values.keys())
        self.assertEqual(keys, user_errors_api, "Las listas no son iguales.")



    def test_mark_error_when_minor_the_min_value_address(self):

        address_min_values = self.min_values_address

        invalid_data = {
            'address': {key: (value - 1) for key, value in address_min_values.items()}}
        address_errors = self.make_the_type_of_error(invalid_data, 'address')
        address_errors_api = self.filter_errors(
            'min_value', address_min_values, address_errors)
        
        keys = list(address_min_values.keys())
        self.assertEqual(keys, address_errors_api, "Las listas no son iguales.")

    

    def test_mark_error_when_pass_the_max_value_address(self):

        address_max_values = self.max_values_address

        invalid_data = {
            'address': {key: (value + 1) for key, value in address_max_values.items()}}
        address_errors = self.make_the_type_of_error(invalid_data, 'address')
        address_errors_api = self.filter_errors(
            'max_value', address_max_values, address_errors)
        
        keys = list(address_max_values.keys())
        self.assertEqual(keys, address_errors_api, "Las listas no son iguales.")

    
    def test_mark_error_when_pass_the_max_value_user(self):

        users_max_values = self.max_values

        invalid_data = {
            'user': {key: (value + 1) for key, value in users_max_values.items()}}
        user_errors = self.make_the_type_of_error(invalid_data, 'user')
        user_errors_api = self.filter_errors(
            'max_value', users_max_values, user_errors)
        keys = list(users_max_values.keys())
        self.assertEqual(keys, user_errors_api, "Las listas no son iguales.")

    def test_return_error_when_input_is_minor_of_the_rules_minlength_address(self):

        min_lengths = self.min_lengths_address
        invalid_data = {'address': {key: 'a' * (value - 1) for key, value in min_lengths.items()}}
        address_errors = self.make_the_type_of_error(invalid_data, 'address')
        address_errors_api = self.filter_errors(
            'min_length', min_lengths, address_errors)
        keys = list(min_lengths.keys())
        self.assertEqual(keys, address_errors_api,"Las listas no son iguales.")


    def test_return_error_when_input_is_minor_of_the_rules_minlength_user(self):

        users_min_lengths = self.min_lengths

        invalid_data = {
            'user': {key: 'a' * (value -1) for key, value in users_min_lengths.items()}}
                
        user_errors = self.make_the_type_of_error(invalid_data, 'user')
        user_errors_api = self.filter_errors(
            'min_length', users_min_lengths, user_errors)
        keys = list(users_min_lengths.keys())

        self.assertEqual(keys, user_errors_api, "Las listas no son iguales.")

    def test_mark_error_when_pass_the_max_length_user(self):

        invalid_data = {
            'user': {key: 'a' * (value + 1) for key, value in self.max_lengths.items()}}
        user_errors = self.make_the_type_of_error(invalid_data, 'user')
        user_errors_api = self.filter_errors(
            'max_length', self.max_lengths, user_errors)
        keys = list(self.max_lengths.keys())
        self.assertEqual(keys, user_errors_api, "Las listas no son iguales.")

    def test_mark_error_when_pass_the_max_length_address(self):

        max_lengths = self.max_lengths_address
        invalid_data = {'address': {key: 'a' *
                                    (value + 1) for key, value in max_lengths.items()}}
        address_errors = self.make_the_type_of_error(invalid_data, 'address')
        address_errors_api = self.filter_errors(
            'max_length', max_lengths, address_errors)
        keys = list(max_lengths.keys())
        self.assertEqual(keys, address_errors_api,
                         "Las listas no son iguales.")

    def test_mark_error_on_user_blank_fields(self):

        invalid_data = {'user': {'name': '', 'email': ''}}
        user_errors = self.make_the_type_of_error(invalid_data, 'user')
        user_errors_api = self.filter_errors(
            'blank', self.not_allow_blank, user_errors)
        self.assertEqual(self.not_allow_blank, user_errors_api,
                         "Las listas no son iguales.")

    def test_mark_error_on_address_blank_fields(self):

        invalid_data = {'address': {
            key: '' for key in self.not_allow_blank_address}}
        address_errors = self.make_the_type_of_error(invalid_data, 'address')
        address_errors_api = self.filter_errors(
            'blank', self.not_allow_blank_address, address_errors)
        self.assertEqual(self.not_allow_blank_address,
                         address_errors_api, "Las listas no son iguales.")

    def test_mark_error_on_user_required_fields(self):

        invalid_data = {'user': {}, 'address': {}, "products": {}}
        user_errors = self.make_the_type_of_error(invalid_data, 'user')

        required_user_fields = self.required_fields
        filtered_user_errors = list(
            filter(lambda error: error['field'] in required_user_fields, user_errors))
        user_errors_api = [item['field'] for item in filtered_user_errors]
        self.assertEqual(required_user_fields, user_errors_api,
                         "Las listas no son iguales.")

    def test_mark_error_on_address_required_fields(self):

        invalid_data = {'user': {}, 'address': {}, "products": {}}
        address_errors = self.make_the_type_of_error(invalid_data, 'address')

        required_address_fields = self.required_fields_address
        filtered_address_errors = list(
            filter(lambda error: error['field'] in required_address_fields, address_errors))
        address_errors_api = [item['field']
                              for item in filtered_address_errors]
        self.assertEqual(required_address_fields,
                         address_errors_api, "Las listas no son iguales.")

    def make_the_type_of_error(self, invalid_data, key):

        response = self.client.post(
            '/api/orden/compra/', invalid_data, format='json')
        return self.error_type(response, key)

    def filter_errors(self, code, requireds, errors):

        filtered_errors = list(filter(
            lambda error: error['field'] in requireds and error['code'] == code, errors))
        return [item['field'] for item in filtered_errors]

    def error_type(self, response, key):

        field_errors = []
        if key in response.data:
            user_errors = response.data[key]
            for field, errors in user_errors.items():
                for error in errors:
                    code = getattr(error, 'code', None)

                    error_info = {
                        'field': field,
                        'code': code if code else 'No disponible'
                    }

                    field_errors.append(error_info)

        return field_errors

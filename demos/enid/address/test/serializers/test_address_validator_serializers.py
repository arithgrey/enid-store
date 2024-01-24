from django.test import TestCase
from rest_framework.exceptions import ValidationError
from address.serializers.address_validator_serializers import AddressValidatorSerializer
from state.models import State
from faker import Faker
import re
from share_test.tests import ValidatorTest


class TestAddressValidatorSerializer(ValidatorTest):
    
    serializer_class = AddressValidatorSerializer
    required_fields = AddressValidatorSerializer.Meta.required_fields
    not_allow_blank = AddressValidatorSerializer.Meta.not_allow_blank
    max_lengths = AddressValidatorSerializer.Meta.max_lengths
    min_lengths = AddressValidatorSerializer.Meta.min_lengths
    min_lengths = AddressValidatorSerializer.Meta.min_lengths
    min_values = AddressValidatorSerializer.Meta.min_values
    max_values = AddressValidatorSerializer.Meta.max_values   

    POSTAL_CODE_TOO_LONG = 'a'*11
    STREET_TOO_LONG = 'a'*101
    COLONY_TOO_LONG = 'a'*101
    DELEGATION_TOO_LONG = 'a'*101
    CITY_TOO_LONG = 'a'*101
    PHONE_NUMBER_TOO_LONG = 'a'*15

    def setUp(self):
        self.fake = Faker('es_MX')
        state = State.objects.create(id=1,name="CDMX")        
        self.state = state


    def test_number_invalid(self):
        #Debe marcar error siempre que no sea un número
        invalid_values = {            
            "number":'djk77',            
            "number":'djk',  
            "number":'888s8888',     
            "state":'isduifiu'
        }

        for field, value in invalid_values.items():            
            data = {field: value}
            serializer = self.serializer_class(data=data)                            
            self.assertFalse(serializer.is_valid())
            self.assertIn(field, serializer.errors)
            self.assertEqual(serializer.errors[field][0].code, 'invalid')

    def test_valid_address(self):
        
        data = {            
            "postal_code":'08500',            
            "street":'Avenida sur 12',  
            "number":'129',     
            "colony":'Agricola Oriental',
            "delegation_or_municipality":"Iztacalco",
            "city":"CDMX",
            "state":self.state.id,
            "phone_number":"5552967027",
        }        
        serializer = self.serializer_class(data=data)
        self.assertTrue(serializer.is_valid())
        
    def test_multiples_valid_address(self):
        
        for _ in range(1000):
            
            postal_code = self.fake.postcode()
            street = self.fake.street_address()
            number = self.fake.random_int(min=1, max=10000)
            while number < 1:
                number = self.fake.random_int(min=2, max=100)
                                
            colony = self.fake.city_prefix()
            delegation_or_municipality = self.fake.city()
            city=self.fake.city()
            id = self.state.id
            phone_number = self.fake.phone_number().split('x')[0].strip()
            cleaned_phone_number = re.sub(r'[^0-9]', '', phone_number)
            
            address = {
                "postal_code": postal_code,
                "street": street,
                "number": number,
                "colony": colony,
                "delegation_or_municipality": delegation_or_municipality,
                "city": city,
                "state": id,
                "phone_number": cleaned_phone_number,
            }
            
            serializer= self.serializer_class(data=address)     
            if not serializer.is_valid():
                print(f"Error en la dirección {address}: {serializer.errors}")

            self.assertTrue(serializer.is_valid())
            
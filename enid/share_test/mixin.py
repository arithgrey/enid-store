from django.test import TestCase
from rest_framework.test import APIClient
from faker import Faker
from share_test.commons import CommonsTest

class CommonMixinTest(TestCase):
    def setUp(self):
        self.fake = Faker('es_MX')
        self.client = APIClient()        
        self.commons = CommonsTest()        
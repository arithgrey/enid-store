from rest_framework.test import APIClient
from faker import Faker
from share_test.commons import CommonsTest

class CommonMixinTest:
    def setUp(self):
        self.fake = Faker('es_MX')
        self.client = APIClient()        
        self.commons = CommonsTest()        
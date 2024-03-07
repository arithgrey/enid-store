from django.test import TestCase, RequestFactory
from rest_framework import status
from store.models import Store
from django.http import Http404
from store.mixin import StoreIDMixin
from share_test.mixin import CommonMixinTest

class StoreIDMixinTest(CommonMixinTest, TestCase):
    
    def setUp(self):

        super().setUp()        
        self.mixin = StoreIDMixin()
        self.store = self.commons.create_fake_store()
        
    def create_request_with_store_id_header(self, store_id):
        factory = RequestFactory()
        request = factory.post('/')
        request.META['HTTP_X_STORE_ID'] = store_id
        return request
    
    def test_get_store_success(self):        
        
        request = self.create_request_with_store_id_header(self.store.id)
        store = self.mixin.get_store_or_default(request)
        self.assertIsInstance(store, Store)

    def test_missing_store_id_header(self):
                
        request = self.create_request_with_store_id_header(None)
        response = self.mixin.get_store_or_default(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_store_raises_http404(self):
                
        with self.assertRaises(Http404):
            self.mixin.get_store(91)
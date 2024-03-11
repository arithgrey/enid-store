from django.test import TestCase
from rest_framework import status
from share_test.oauth import OAuthUtilities
from share_test.mixin import CommonMixinTest

class OAuthTest(CommonMixinTest):

    def setUp(self):
        super().setUp()
        self.api = None
        self.method = None
        self.oauthUtilities = OAuthUtilities()
        self.store = self.commons.create_fake_store()
        self.headers =self.commons.add_headers_store(store=self.store)

    def execute_request(self, api_client ,method, api_url, data=None):
        """
        Execute an HTTP request using the provided method (GET, POST, PUT, DELETE) on a API clients.
        """                
        switch = {
            'get': api_client.get,
            'post': api_client.post,
            'put': api_client.put,
            'delete': api_client.delete,
        }

        
        request_function = switch.get(method.lower())
        
        if request_function is None:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        
        response = request_function(api_url, data, format='json', **self.headers)        

        return response


    def test_authenticated_user(self):
        
        if self.api is not None: 
            
            _, api_client = self.oauthUtilities.fake_user_and_api_client()

            response = self.execute_request(
                api_client=api_client,  method=self.method, api_url=self.api)
            
            self.assertNotEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
            self.assertNotEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
    


    def test_unauthenticated_user(self):
        
        if self.api is not None:                 
            response = self.execute_request(
                api_client=self.client,  method=self.method, api_url=self.api)
            
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
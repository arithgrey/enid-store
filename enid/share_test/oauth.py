from share_test.mixin import CommonMixinTest
from rest_framework_simplejwt.tokens import AccessToken
from store.models import Store

class OAuthUtilities(CommonMixinTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setUp()

    def fake_user_and_api_client(self, **kwargs):
        
        user  = self.commons.crear_fake_user(**kwargs)
        access_token = AccessToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        return user, self.client    
    
    def fake_user_and_api_client_with_headers(self, store, **kwargs):

        user, api_client = self.fake_user_and_api_client(**kwargs)
        headers = HeaderUtilities.add_headers_store(store)
        for key, value in headers.items():
            api_client.defaults[key] = value
            
        return user, api_client


class HeaderUtilities:
    def __init__(self, store):
        self.headers = self.add_headers_store(store)

    @staticmethod
    def add_headers_store(store):
        if isinstance(store, Store):
            store_id = store.id
            return {'HTTP_X_STORE_ID': store_id}
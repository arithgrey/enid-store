from share_test.mixin import CommonMixinTest
from rest_framework_simplejwt.tokens import AccessToken

class OAuthUtilities(CommonMixinTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setUp()

    def fake_user_and_api_client(self, **kwargs):
        
        user  = self.commons.crear_fake_user(**kwargs)
        access_token = AccessToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        return user, self.client
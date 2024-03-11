from rest_framework import status
from rest_framework.response import Response
from store.models import Store
from django.shortcuts import get_object_or_404
from user.oauth_utils import AuthenticationChecker
class StoreIDMixin:

    @staticmethod
    def get_store_or_default(request):
        store_id = StoreIDMixin.validate_store_id(request)
        
        if store_id is not None:
            store = StoreIDMixin.get_store(store_id)
            return store
        
        return Response({'error': 'X-Store-Id header is missing'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def validate_store_id(request):
        store_id = request.headers.get('X-Store-Id')
        
        if store_id is None:
            return None
        
        return store_id

    @staticmethod
    def get_store(store_id):
        store = get_object_or_404(Store, id=store_id)
        return store


class StoreAuthenticationMixin:
    @staticmethod
    def get_store_or_default(request):
        authentication_error = AuthenticationChecker.check_authentication(request)
        if authentication_error:
            return authentication_error
        
        return StoreIDMixin.get_store_or_default(request=request)

    
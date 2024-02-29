from rest_framework import status
from rest_framework.response import Response
from store.models import Store
from django.shortcuts import get_object_or_404

class StoreIDMixin:

    def get_store_or_default(self, request):
        store_id = self.validate_store_id(request)
        
        if store_id is not None:
            store = self.get_store(store_id)
            return store
        
        return Response({'error': 'X-Store-Id header is missing'}, status=status.HTTP_400_BAD_REQUEST)


    def validate_store_id(self, request):
        store_id = request.headers.get('X-Store-Id')
        
        if store_id is None:
            return None
        
        return store_id

    def get_store(self, store_id):
        store = get_object_or_404(Store, id=store_id)
        return store

from rest_framework import viewsets
from rest_framework.response import Response
from django.core.cache import cache
from categories.serializers import CategorySerializer
from categories.models import Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'categories_list'
        cache_data = cache.get(cache_key)
        if cache_data is not None:
            return Response(cache_data)
            
        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=60 * 60 * 240)
        return response

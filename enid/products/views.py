from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from products.models import Product
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from categories.models import Category
from search.views import CustomPageNumberPagination
from django.core.cache import cache

class ProductVuewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination

    @action(detail=False, methods=['GET'], url_path='top-sellers')
    def top_sellers(self, request):        
        
        top_sellers = cache.get('top_sellers')        
        if not top_sellers:            
            top_sellers = Product.objects.filter(top_seller=True).order_by('id')
            cache.set('top_sellers', top_sellers, timeout=3600)
        
        
        page = self.paginate_queryset(top_sellers)        

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductSerializer(top_sellers, many=True)
        
        return Response(serializer.data)


class ProductSlugVuewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=True, methods=['GET'])    
    def get_by_slug(self, request, category_slug, product_slug):
        
        cache_key = f"product_{category_slug}_{product_slug}"
        cached_data = cache.get(cache_key)

        if cached_data:            
            return Response(cached_data)

        category = get_object_or_404(Category, slug=category_slug)
        product = get_object_or_404(Product, category=category, slug=product_slug)

        serializer = ProductSerializer(product)
        serializer_data= serializer.data
        cache.set(cache_key, serializer_data, timeout=3600)

        return Response(serializer_data)
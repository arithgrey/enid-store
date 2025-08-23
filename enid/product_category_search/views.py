from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from products.models import Product
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from categories.models import Category
from search.views import CustomPageNumberPagination
from django.core.cache import cache

class ProducByCategorySlugViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination

    @action(detail=True, methods=['GET'])
    def get_by_category_slug(self, request, category_slug):
        # Usar request.GET para acceder a los parámetros de query
        page_number = request.GET.get('page', 1)
        # Actualizar la clave del cache para incluir el filtro de productos públicos
        cache_key = f"product_{category_slug}_public_page_{page_number}"
        cache_data = cache.get(cache_key)
        if cache_data:
            return Response(cache_data)

        category = get_object_or_404(Category, slug=category_slug)
        # Filtrar solo productos públicos de la categoría
        products = Product.objects.filter(
            category=category, 
            es_publico=True
        ).order_by("id")

        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)            
            cache.set(cache_key, response.data, timeout=86400)
            return response

        serializer = ProductSerializer(products, many=True)
        response = Response(serializer.data)
        cache.set(cache_key, response.data, timeout=86400)
        return response
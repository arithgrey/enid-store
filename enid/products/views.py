from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from products.models import Product
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from categories.models import Category
from search.views import CustomPageNumberPagination
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)

class ProductVuewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination

    def create(self, request, *args, **kwargs):
        try:
            logger.info(f"Creating product with data: {request.data}")
            
            # Validar datos básicos
            errors = {}
            required_fields = ['name', 'specific_name', 'price', 'category']
            for field in required_fields:
                if field not in request.data:
                    errors[field] = 'Este campo es requerido'
            
            if errors:
                return Response(errors, status=400)
            
            response = super().create(request, *args, **kwargs)
            logger.info(f"Product created successfully: {response.data}")
            return response
            
        except Exception as e:
            logger.error(f"Error creating product: {str(e)}")
            if hasattr(e, 'detail'):
                return Response(e.detail, status=400)
            return Response({'error': str(e)}, status=400)

    @action(detail=False, methods=['GET'], url_path='top-sellers')
    def top_sellers(self, request):        
          
        cache_key = f'top_sellers_public_'
        top_sellers = cache.get(cache_key)        
        if not top_sellers:            
            # Filtrar solo productos top_seller que sean públicos
            top_sellers = Product.objects.filter(
                top_seller=True, 
                es_publico=True
            ).order_by('id')
            cache.set(cache_key, top_sellers, timeout=86400)
        
        
        page = self.paginate_queryset(top_sellers)        

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductSerializer(top_sellers, many=True)
        
        return Response(serializer.data)

    @action(detail=False, methods=['GET'], url_path='primary-products')
    def primary_products(self, request):        
        # También filtrar productos primarios que sean públicos
        primary_products = Product.objects.filter(
            primary=True, 
            es_publico=True
        ).order_by('id')
        serializer = ProductSerializer(primary_products, many=True)        
        return Response(serializer.data)

class ProductSlugVuewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=True, methods=['GET'])    
    def get_by_slug(self, request, category_slug, product_slug):
        es_landing = request.query_params.get('es_landing', False) 
        cache_key = f"product_{category_slug}_{product_slug}_public_"
        cached_data = cache.get(cache_key)

        if cached_data and not es_landing:             
            return Response(cached_data)

        category = get_object_or_404(Category, slug=category_slug)
        if es_landing:
            product = get_object_or_404(    
                Product, 
                category=category, 
                slug=product_slug
            )
        else:
            # Solo permitir acceso a productos públicos
            product = get_object_or_404(
                Product, 
                category=category, 
                slug=product_slug,
                es_publico=True
            )
                
        serializer = ProductSerializer(product)
        serializer_data= serializer.data
        cache.set(cache_key, serializer_data, timeout=86400)

        return Response(serializer_data)
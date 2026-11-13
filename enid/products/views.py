from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.serializers import ModelSerializer
from django.utils import timezone
from django.db import transaction
from order.models import Order
from item_order.models import ItemOrder
from revenue.constants import RECIBIDOS
from products.models import Product, PaymentMethod
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

    ALLOWED_TRANSITIONS = {
        'published': {'candidate', 'certified'},
        'candidate': {'certified', 'published'},
        'certified': {'candidate', 'published'},
    }

    @action(detail=True, methods=['patch'], url_path='certification',
            permission_classes=[IsAdminUser])
    def certification(self, request, pk=None):
        product = self.get_object()
        target = request.data.get('certification')
        valid = dict(Product.CERTIFICATION_CHOICES)
        if target not in valid:
            return Response({'error': 'Estado de certificación inválido'}, status=400)
        if target != product.certification and target not in self.ALLOWED_TRANSITIONS[product.certification]:
            return Response(
                {'error': f'Transición no permitida: {product.certification} → {target}'},
                status=400,
            )
        product.certification = target
        product.certified_at = timezone.now() if target == 'certified' else None
        product.save(update_fields=['certification', 'certified_at'])
        return Response(ProductSerializer(product).data)

    @action(detail=False, methods=['post'], url_path='manual-sale',
            permission_classes=[IsAdminUser])
    def manual_sale(self, request):
        items = request.data.get('items') or []
        status_val = request.data.get('status', 'delivered')
        sale_date = request.data.get('sale_date') or None

        if not items:
            return Response({'error': 'Se requiere al menos un item'}, status=400)
        if status_val not in RECIBIDOS:
            return Response(
                {'error': f'status inválido; usar uno de {RECIBIDOS}'}, status=400
            )
        # Validar productos antes de crear nada
        resolved = []
        for it in items:
            product = Product.objects.filter(pk=it.get('product')).first()
            if not product:
                return Response({'error': 'Producto inexistente'}, status=400)
            resolved.append((product, it.get('quantity', 1), it.get('price')))

        with transaction.atomic():
            order = Order.objects.create(
                status=status_val, source='admin_manual', sale_date=sale_date
            )
            for product, quantity, price in resolved:
                ItemOrder.objects.create(
                    order=order, product=product, quantity=quantity, price=price
                )
        return Response({'order_id': order.id, 'status': order.status}, status=201)

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


class PaymentMethodSerializer(ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['slug', 'name']


class PaymentMethodListView(generics.ListAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from products.models import Product
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from categories.models import Category

class ProductVuewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['GET'], url_path='top-sellers')
    def top_sellers(self, request):        
        top_sellers = Product.objects.filter(top_seller=True)[:6]
        serializer = ProductSerializer(top_sellers, many=True)
        
        return Response(serializer.data)


class ProductSlugVuewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=True, methods=['GET'])    
    def get_by_slug(self, request, category_slug, product_slug):
        
        category = get_object_or_404(Category, slug=category_slug)
        product = get_object_or_404(Product, category=category, slug=product_slug)

        serializer = ProductSerializer(product)
        return Response(serializer.data)
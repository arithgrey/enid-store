from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from products.models import Product
from products.serializers import ProductSerializer

class ProductVuewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['GET'], url_path='top-sellers')
    def top_sellers(self, request):        
        top_sellers = Product.objects.filter(top_seller=True)[:6]
        serializer = ProductSerializer(top_sellers, many=True)
        
        return Response(serializer.data)
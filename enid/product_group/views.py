from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from product_group.models import ProductGroup
from rest_framework.decorators import action
from product_group.serializers import ProductGroupSerializer
from products.serializers import ProductItemSerializer
from django.shortcuts import get_object_or_404
    
class ProductGroupViewSet(viewsets.ModelViewSet):

    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer 
   
    @action(detail=True, methods=['GET'])
    def get_products(self,request, pk=None):
                
        product_group = get_object_or_404(ProductGroup, id=pk)
        serializer = ProductGroupSerializer(product_group)
        return Response(serializer.data)
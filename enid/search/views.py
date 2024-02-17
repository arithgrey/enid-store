from rest_framework import viewsets, pagination
from rest_framework.response import Response
from rest_framework.decorators import action
from products.models import Product
from rest_framework import status
from products.serializers import ProductSerializer
from search.serializers import SearchValidatorSerializer
from django.db.models import Q

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ProductSeachByQViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    pagination_class = CustomPageNumberPagination
    
    @action(detail=False, methods=['GET'])    
    def get_by_q(self, request, q):
                
        data = {'q':q}
        serializer = SearchValidatorSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
        
        
        products = self.perform_search(q)
        products = products.order_by('id')
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = ProductSerializer(page, many=True)    
            return self.get_paginated_response(serializer.data)


        serializer = ProductSerializer(products, many=True)    
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def perform_search(self,q):
        return Product.objects.filter(
            Q(specific_name__icontains=q) |        
            Q(name__icontains=q) |            
            Q(category__name__icontains=q)            
        )

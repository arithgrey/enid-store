# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, pagination
from rest_framework.response import Response
from rest_framework.decorators import action
from business.models import Business
from image.serializers import ImageSerializer

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 1000


class BusinessSlugImagesViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = ImageSerializer
    pagination_class = CustomPageNumberPagination


    @action(detail=True, methods=['GET'])
    def images_by_slug(self, request, business_slug):        
        business = get_object_or_404(Business, slug=business_slug)
        images = business.images.all()
        
        page = self.paginate_queryset(images)
        if page is not None:
            serializer = ImageSerializer(page, many=True)    
            return self.get_paginated_response(serializer.data)

        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)    
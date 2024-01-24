from django.shortcuts import render
from rest_framework import viewsets
from image.serializers import ImageSerializer
from image.models import Image

class ImageViewSet(viewsets.ModelViewSet):
    
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
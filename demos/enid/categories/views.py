from rest_framework import viewsets
from rest_framework.response import Response
from categories.serializers import CategorySerializer
from categories.models import Category

class CategoryVuewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
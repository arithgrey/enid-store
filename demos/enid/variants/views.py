from django.shortcuts import render
from rest_framework import viewsets
from variants.models import Variant
from variants.serializers import VariantSerializer

# Create your views here.
class VariantVuewSet(viewsets.ModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
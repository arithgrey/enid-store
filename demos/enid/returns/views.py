from django.shortcuts import render
from returns.serializers import ReturnsSerializer
from rest_framework import viewsets
from .models import Returns

# Create your views here.
class ReturnsViewSet(viewsets.ModelViewSet):

    queryset = Returns.objects.all()
    serializer_class = ReturnsSerializer
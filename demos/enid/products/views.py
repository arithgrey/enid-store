from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, ItemCard, Card
from products.serializers import ProductSerializer, ItemCardSerializer, CardSerializer
# Create your views here.
class ProductVuewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ItemCardVuewSet(viewsets.ModelViewSet):
    queryset = ItemCard.objects.all()
    serializer_class = ItemCardSerializer

class CardVuewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

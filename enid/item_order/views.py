from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from item_order.models import ItemOrder
from item_order.serializer import ItemOrderSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class ItemOrderViewSet(viewsets.ModelViewSet):
        
    queryset = ItemOrder.objects.all()
    serializer_class = ItemOrderSerializer
    lookup_field = 'id'

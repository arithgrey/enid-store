from rest_framework import viewsets
from item_cart.serializers import ItemCartSerializer
from item_cart.models import ItemCart

# Create your views here.
class ItemCartVuewSet(viewsets.ModelViewSet):
    queryset = ItemCart.objects.all()
    serializer_class = ItemCartSerializer


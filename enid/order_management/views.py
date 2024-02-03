from rest_framework import viewsets
from rest_framework.response import Response
from order_management.serializers import OrderSerializer
from order.models import Order

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
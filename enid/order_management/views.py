from rest_framework import viewsets
from order_management.serializers import OrderSerializer
from order.models import Order
from notifications.client import notify_order

_NOTIFY_STATUSES = {'payment_confirmed', 'delivered'}


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_update(self, serializer):
        old_status = self.get_object().status
        instance = serializer.save()
        if instance.status != old_status and instance.status in _NOTIFY_STATUSES:
            notify_order(instance.status, instance)
    
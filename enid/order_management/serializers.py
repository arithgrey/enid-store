from rest_framework import serializers
from order.models import Order
from item_order.serializer import ItemOrderSerializer
from order.serializer_status import BaseOrderSerializer
class OrderSerializer(BaseOrderSerializer):  
    class Meta(BaseOrderSerializer.Meta):
        ref_name = 'OrderManagementOrder'
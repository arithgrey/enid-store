from rest_framework import serializers
from order.models import Order
from item_order.serializer import ItemOrderSerializer
class OrderSerializer(serializers.ModelSerializer):  

    items = ItemOrderSerializer(many=True, read_only=True) 

    class Meta:
        model = Order
        fields = '__all__'
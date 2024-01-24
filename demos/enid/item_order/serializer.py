from rest_framework import serializers
from item_order.models import ItemOrder


class ItemOrderSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ItemOrder
        fields = '__all__'
        
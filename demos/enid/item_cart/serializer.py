from rest_framework import serializers
from item_order.models import itemOrder


class OrderSerializer(serializers.ModelSerializer):    
    class Meta:
        model = itemOrder
        fields = '__all__'
        
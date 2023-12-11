from django.utils.translation import gettext as _
from rest_framework import serializers
from products.serializers import ProductSerializer
from item_cart.models import ItemCart

class ItemCartSerializer(serializers.ModelSerializer):    
    product = ProductSerializer()
   
    class Meta:
        model = ItemCart
        fields = '__all__'


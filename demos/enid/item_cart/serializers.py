from django.utils.translation import gettext as _
from rest_framework import serializers
from item_cart.models import ItemCart

class ItemCartSerializer(serializers.ModelSerializer):    
   
    product_name = serializers.CharField(source='product.name', read_only=True, label=_('Product Name'))
    quantity = serializers.IntegerField(label=_('Quantity'))
    
    class Meta:
        model = ItemCart
        fields = '__all__'


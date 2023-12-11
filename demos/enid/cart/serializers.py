from django.utils.translation import gettext as _
from rest_framework import serializers
from item_cart.serializers import ItemCartSerializer
from cart.models import Cart

class CartSerializer(serializers.ModelSerializer):
    product = ItemCartSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

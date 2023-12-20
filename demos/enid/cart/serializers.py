from django.utils.translation import gettext as _
from rest_framework import serializers
from cart.models import Cart

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'

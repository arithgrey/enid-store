from rest_framework import serializers
from order.models import Order
from user.serializers.user_validator_serializers import UserValidatorSerializer
from address.serializers.address_validator_serializers import AddressValidatorSerializer

class OrderSerializer(serializers.ModelSerializer):    

    class Meta:
        model = Order
        fields = '__all__'
        ref_name = 'Order'
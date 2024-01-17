from rest_framework import serializers
from order.models import Order
from user.serializers.user_validator_serializers import UserValidatorSerializer
from address.serializers.address_validator_serializers import AddressValidatorSerializer

class OrderSerializer(serializers.ModelSerializer):    
    #user = UserValidatorSerializer(required=True)
    #address = AddressValidatorSerializer(required=True)

    class Meta:
        model = Order
        fields = '__all__'
from rest_framework import serializers
from order.models import Order
from user.serializers.user_validator_serializers import UserValidatorSerializer
from address.serializers.address_validator_serializers import AddressValidatorSerializer

class OrderSerializer(serializers.ModelSerializer):    
    source_display = serializers.CharField(source='source', read_only=True, help_text="Fuente de origen de la orden")

    class Meta:
        model = Order
        fields = '__all__'
        ref_name = 'Order'
from rest_framework import serializers
from address.models import Address
from state.serializers import StateSerializer 
from user.serializers.user_serializers import UserSerializer


class AddressSerializer(serializers.ModelSerializer):    
    
    state = StateSerializer(read_only=True)
    user = UserSerializer(read_only=True)      
    
    class Meta:
        model = Address
        fields = '__all__'
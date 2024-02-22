from rest_framework import serializers
from lead_type.models import LeadType

class LeadTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LeadType
        fields = '__all__'

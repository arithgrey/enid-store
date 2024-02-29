# serializers.py
from rest_framework import serializers
from lead.models import Lead


class LeadSearchSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(source='products_interest', many=True, read_only=True)

    class Meta:
        model = Lead
        fields = ['id', 'name', 'email', 'phone_number', 'status','created_at','products']
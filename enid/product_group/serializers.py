from rest_framework import serializers
from product_group.models import ProductGroup
from products.serializers import ProductItemSerializer


class ProductGroupSerializer(serializers.ModelSerializer):    
    products = ProductItemSerializer(many=True, read_only=True)
    class Meta:
        model = ProductGroup
        fields = '__all__'
        
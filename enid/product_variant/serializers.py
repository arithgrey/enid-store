from rest_framework import serializers
from product_variant.models import ProductVariant
from variants.serializers import VariantSerializer
class ProductVariantSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = ProductVariant
        fields = '__all__'

class ProductVariantByProductSerializer(serializers.ModelSerializer):
    variant = VariantSerializer()

    class Meta:
        model = ProductVariant
        fields = '__all__'

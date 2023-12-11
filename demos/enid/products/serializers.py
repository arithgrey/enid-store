from django.utils.translation import gettext as _
from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):

    short_name = serializers.SerializerMethodField()
    formatted_price = serializers.SerializerMethodField()
    formatted_weight = serializers.SerializerMethodField()

    class Meta:
        model = Product        
        fields = '__all__'
    
    def get_short_name(self, obj):
        return obj.name[:82] if obj.name else ''

    def get_formatted_price(self, obj):
        return _('${:.2f}').format(obj.price)
    
    def get_formatted_weight(self, obj):
        return f"{obj.weight} Kg"
    

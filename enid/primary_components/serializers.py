from rest_framework import serializers
from .models import ProductComponent
from products.models import Product

class ProductComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComponent
        fields = ['id', 'kit', 'component', 'quantity']
        
    def validate(self, data):
        # Verificar que el producto no se agregue a sí mismo como componente
        if data['kit'] == data['component']:
            raise serializers.ValidationError(
                "Un producto no puede ser componente de sí mismo"
            )
        return data

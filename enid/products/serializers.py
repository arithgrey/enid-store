from django.utils.translation import gettext as _
from rest_framework import serializers
from products.models import Product
from image.serializers import ImageSerializer
from categories.serializers import CategorySerializer
from categories.models import Category

class ProductItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()     
    class Meta:
        model = Product        
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    short_name = serializers.SerializerMethodField()
    formatted_price = serializers.SerializerMethodField()
    formatted_cost = serializers.SerializerMethodField()
    formatted_weight = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)     
    
    class Meta:
        model = Product        
        fields = '__all__'
    
    def create(self, validated_data):
        # Manejar la creación de categoría si se proporciona un ID
        if 'category' in self.initial_data:
            try:
                category_id = self.initial_data['category']
                category = Category.objects.get(id=category_id)
                validated_data['category'] = category
            except (Category.DoesNotExist, ValueError, TypeError):
                raise serializers.ValidationError({'category': 'La categoría especificada no existe'})
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        # Manejar la actualización de categoría si se proporciona
        if 'category' in self.initial_data:
            try:
                category_id = self.initial_data['category']
                category = Category.objects.get(id=category_id)
                instance.category = category
            except (Category.DoesNotExist, ValueError, TypeError):
                pass  # Si hay error, ignoramos el cambio de categoría
        
        # Actualizar los demás campos normalmente
        return super().update(instance, validated_data)
    
    def get_short_name(self, obj):
        return obj.name[:82] if obj.name else ''

    def get_formatted_price(self, obj):
        return _('${:.2f}').format(obj.price)
    
    def get_formatted_weight(self, obj):
        return f"{obj.weight} Kg"
    
    def get_formatted_cost(self, obj):
        return _('${:.2f}').format(obj.cost)

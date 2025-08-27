from django.utils.translation import gettext as _
from rest_framework import serializers
from products.models import Product
from image.serializers import ImageSerializer
from categories.serializers import CategorySerializer
from categories.models import Category
from image.models import Image
from django.contrib.contenttypes.models import ContentType

class ProductItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()     
    class Meta:
        model = Product        
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )
    main_image_index = serializers.IntegerField(write_only=True, required=False)
    short_name = serializers.SerializerMethodField()
    formatted_price = serializers.SerializerMethodField()
    formatted_cost = serializers.SerializerMethodField()
    formatted_weight = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)     
    
    class Meta:
        model = Product        
        fields = '__all__'
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        main_image_index = validated_data.pop('main_image_index', 0)
        
        # Manejar la creación de categoría si se proporciona un ID
        if 'category' in self.initial_data:
            try:
                category_id = self.initial_data['category']
                category = Category.objects.get(id=category_id)
                validated_data['category'] = category
            except (Category.DoesNotExist, ValueError, TypeError):
                raise serializers.ValidationError({'category': 'La categoría especificada no existe'})
        
        # Crear el producto
        product = super().create(validated_data)
        
        # Obtener el content type para el producto
        product_content_type = ContentType.objects.get_for_model(product)
        
        # Crear las imágenes asociadas
        for index, image_file in enumerate(uploaded_images):
            Image.objects.create(
                content_type=product_content_type,
                object_id=product.id,
                image=image_file,
                is_main=(index == main_image_index)
            )
        
        return product
    
    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        main_image_index = validated_data.pop('main_image_index', None)
        
        # Manejar la actualización de categoría si se proporciona
        if 'category' in self.initial_data:
            try:
                category_id = self.initial_data['category']
                category = Category.objects.get(id=category_id)
                instance.category = category
            except (Category.DoesNotExist, ValueError, TypeError):
                pass  # Si hay error, ignoramos el cambio de categoría
        
        # Actualizar el producto
        instance = super().update(instance, validated_data)
        
        # Si hay nuevas imágenes, agregarlas
        if uploaded_images:
            product_content_type = ContentType.objects.get_for_model(instance)
            
            # Si se especifica una nueva imagen principal, desmarcar la anterior
            if main_image_index is not None:
                instance.images.filter(is_main=True).update(is_main=False)
            
            # Crear las nuevas imágenes
            for index, image_file in enumerate(uploaded_images):
                Image.objects.create(
                    content_type=product_content_type,
                    object_id=instance.id,
                    image=image_file,
                    is_main=(index == main_image_index if main_image_index is not None else False)
                )
        
        return instance
    
    def get_short_name(self, obj):
        return obj.name[:82] if obj.name else ''

    def get_formatted_price(self, obj):
        return _('${:.2f}').format(obj.price)
    
    def get_formatted_weight(self, obj):
        return f"{obj.weight} Kg"
    
    def get_formatted_cost(self, obj):
        return _('${:.2f}').format(obj.cost)

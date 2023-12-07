from rest_framework import serializers
from products.models import  Product, Card, ItemCard

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'        
    
class ItemCardSerializer(serializers.ModelSerializer):    
    product = ProductSerializer()
   
    class Meta:
        model = ItemCard
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    product =  ItemCardSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = '__all__'

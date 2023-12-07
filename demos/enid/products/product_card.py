from .models import ItemCard
from .interfaces import ProductCardHandler

#Agrega productos al carro de compras, esta es la implementación por default 
class DefaultProductCard(ProductCardHandler):
    def add_product(self, card, product, amount):
        return ItemCard.objects.create(card=card, product=product, amount=amount)
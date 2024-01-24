from item_cart.models import ItemCart
from products.interfaces import ProductCartHandler

#Agrega productos al carro de compras, esta es la implementación por default 
class DefaultProductCart(ProductCartHandler):
    def add_product(self, cart, product, amount):
        return ItemCart.objects.create(cart=cart, product=product, amount=amount)
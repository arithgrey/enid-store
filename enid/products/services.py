#Servicio par agregar productos al carro de compras (Ver implementaciones en product_cart.py) 
class ServiceProductCart:
    def __init__(self, product_cart_handler):
        self.product_cart_handler = product_cart_handler

    def add_product(self, cart, product, amount):
        self.product_cart_handler.add_product(cart, product, amount)
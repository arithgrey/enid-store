#Servicio par agregar productos al carro de compras (Ver implementaciones en product_card.py) 
class ServiceProductCard:
    def __init__(self, product_card_handler):
        self.product_card_handler = product_card_handler

    def add_product(self, card, product, amount):
        self.product_card_handler.add_product(card, product, amount)
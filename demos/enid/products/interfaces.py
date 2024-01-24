from abc import ABC, abstractclassmethod

class ProductCartHandler(ABC):
    
    @abstractclassmethod
    def add_product(self, cart, product, amount):
        pass
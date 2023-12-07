from abc import ABC, abstractclassmethod

class ProductCardHandler(ABC):
    
    @abstractclassmethod
    def add_product(self, card, product, amount):
        pass
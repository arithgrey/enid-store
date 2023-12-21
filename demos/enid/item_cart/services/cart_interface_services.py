from abc import ABC, abstractmethod

class CartServiceInterface(ABC):
    @abstractmethod
    def get_or_create_cart(self, session):

        pass
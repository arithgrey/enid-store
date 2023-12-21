from django.db import models
from cart.models import Cart
from products.models import Product
# Create your models here.

#Cada elemento del carro tiene la referencia del producto, cantidad y el carro de compras al que pertenece 
class ItemCart(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
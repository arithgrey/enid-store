from django.db import models
from django.contrib.auth.models import User
from products.models import Product

#Un carro de compras puede tener varios productos   
class Cart(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='item_cart.ItemCart')
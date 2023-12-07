from django.db import models
from django.contrib.auth.models import User

# models
class Product(models.Model):
    
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

#Un carro de compras puede tener varios productos   
class Card(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='ItemCard')

#Cada elemento del carro tiene la referencia del producto, cantidad y el carro de compras al que pertenece 
class ItemCard(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    
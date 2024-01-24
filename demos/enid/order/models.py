from django.db import models
from django.contrib.auth.models import User
from address.models import Address
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pendiente'),
        ('shipped', 'Enviada'),
        ('completed', 'Completada'),
        ('canceled', 'Cancelada'),
    )

    shipping_address = models.ForeignKey(Address, related_name='order_address', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')        
    user = models.ForeignKey(User, related_name='user_order', on_delete=models.CASCADE, null=True, blank=True)
    #transaction_id = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"Order {self.id}"
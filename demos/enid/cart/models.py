from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone


#Un carro de compras puede tener varios productos   
class Cart(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    unique_identifier = models.CharField(max_length=255, unique=True, default='enid')
    created_at = models.DateTimeField(default=timezone.now, editable=False)

# variants/models.py
from django.db import models

class Variant(models.Model):
    name = models.CharField(max_length=50)
    weight = models.DecimalField(default=0.5, max_digits=5, decimal_places=2)
    long = models.DecimalField(default=0, max_digits=5, decimal_places=2)    
    disc = models.BooleanField(default=False)    
    
    def __str__(self):
        return self.name
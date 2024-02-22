from django.db import models
from lead_type.models import LeadType
from products.models import Product

class Lead(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)    
    lead_type = models.ForeignKey(LeadType, related_name='lead_type', on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    tryet = models.IntegerField(default=1, null=False)
    products_interest = models.ManyToManyField(Product, related_name='products_interest')

    def __str__(self):
        return self.name
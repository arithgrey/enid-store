from django.db import models
from products.models import Product
from variants.models import Variant

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    pieces = models.PositiveIntegerField(default=1)

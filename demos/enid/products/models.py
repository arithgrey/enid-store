
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(default=0.5, max_digits=5, decimal_places=2)        
    path_main_image = models.URLField(null=True)
    count_discs = models.BooleanField(default=False)
    #variants = models.ManyToManyField('variants.Variant', related_name='product_variants')

    def __str__(self):
        return self.name

from categories.models import Category
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from image.models import Image
from autoslug import AutoSlugField
from product_group.models import ProductGroup  
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

class Product(models.Model):
    
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(default=0.5, max_digits=5, decimal_places=2)            
    count_discs = models.BooleanField(default=False)
    top_seller = models.BooleanField(default=False)
    slug = AutoSlugField(unique=True, populate_from='name')
    specific_name = models.CharField(max_length=250)
    product_group = models.ForeignKey(
         ProductGroup, related_name='products', on_delete=models.SET_NULL, default=None, null=True)
    name_product_group = models.CharField(max_length=50, default=None, null=True, blank=True)    
    images = GenericRelation(Image)
    express_payment_link = models.URLField(max_length=500, null=True, blank=True)

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
            return f"{self.category.slug}/{self.slug}/"

@receiver(post_save, sender=Product)
def clear_product_cache(sender, instance, **kwargs):
    #aplico el delete del indice de deredis para que se actualice el cache
    cache.delete_pattern("product_*")
    cache.delete_pattern("top_sellers_*")
from categories.models import Category
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from image.models import Image
from autoslug import AutoSlugField
from product_group.models import ProductGroup  
from store.models import Store
class Product(models.Model):
    
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
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

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
            return f"{self.category.slug}/{self.slug}/"
        
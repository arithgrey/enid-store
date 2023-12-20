from categories.models import Category
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from image.models import Image

class Product(models.Model):

    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(default=0.5, max_digits=5, decimal_places=2)            
    count_discs = models.BooleanField(default=False)
    top_seller = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    images = GenericRelation(Image)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
            return f"{self.category.slug}/{self.slug}/"
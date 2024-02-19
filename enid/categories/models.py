from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = AutoSlugField(unique=True, populate_from='name')
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
            return f"/{self.slug}/"

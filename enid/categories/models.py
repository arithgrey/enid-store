from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):    
    name = models.CharField(max_length=200)
    video_name = models.CharField(max_length=200, blank=True, null=True)
    slug = AutoSlugField(unique=True, populate_from='name')    
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
            return f"/{self.slug}/"

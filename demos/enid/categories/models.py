from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)    
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
            return f"/{self.slug}/"

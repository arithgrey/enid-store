from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings
from autoslug import AutoSlugField

class Image(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,null=True, blank=True)
    object_id = models.PositiveIntegerField(default=1)
    content_object = GenericForeignKey('content_type', 'object_id')

    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)  
    image = models.ImageField(upload_to='') 
    is_main = models.BooleanField(default=False)

    
    def __str__(self):
        return self.title or f"Imagen {self.id}"

    def get_image_url(self):
        
        if settings.DOMAIN:                        
            return f"{settings.DOMAIN}{self.image.url}"


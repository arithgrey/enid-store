from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from image.models import Image
from autoslug import AutoSlugField

class Business(models.Model):
    name = models.CharField(max_length=100)
    images = GenericRelation(Image)
    slug = AutoSlugField(unique=True, populate_from='name')

    def __str__(self):
        return self.name
from django.db import models

class ProductGroup(models.Model):   
   name = models.CharField(max_length=200)
   category = models.CharField(max_length=50, default=None, null=True, blank=True)    
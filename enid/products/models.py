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
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weight = models.DecimalField(default=0.5, max_digits=5, decimal_places=2)            
    count_discs = models.BooleanField(default=False)
    top_seller = models.BooleanField(default=False)
    primary = models.BooleanField(default=False)
    slug = AutoSlugField(unique=True, populate_from='name')
    specific_name = models.CharField(max_length=250)
    product_group = models.ForeignKey(
         ProductGroup, related_name='products', on_delete=models.SET_NULL, default=None, null=True)
    name_product_group = models.CharField(max_length=50, default=None, null=True, blank=True)    
    images = GenericRelation(Image)
    express_payment_link = models.URLField(max_length=500, null=True, blank=True)
    
    # Campos para manejo de inventario
    min_stock = models.IntegerField(default=1)
    max_stock = models.IntegerField(default=100)
    
    # Campo para control de visibilidad pública
    es_publico = models.BooleanField(default=True, help_text='Indica si el producto es visible públicamente')
    
    primary_components = models.ManyToManyField(
        'self',
        through='primary_components.ProductComponent',
        symmetrical=False,
        related_name='kit_products',
        blank=True,
        help_text='Productos primarios que componen este kit'
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
            return f"{self.category.slug}/{self.slug}/"

    def is_weight_kit(self):
        """
        Determina si el producto es un kit de pesas verificando si tiene
        productos primarios asociados
        """
        return self.primary_components.exists()

    def get_primary_products(self):
        """
        Retorna los productos primarios que componen este kit con sus cantidades
        """
        return self.component_quantities.all()

@receiver(post_save, sender=Product)
def clear_product_cache(sender, instance, **kwargs):
    #aplico el delete del indice de deredis para que se actualice el cache
    cache.delete_pattern("product_*")
    cache.delete_pattern("top_sellers_*")
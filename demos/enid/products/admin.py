from django.contrib import admin
from .models import Product, Card, ItemCard
# Register your models here.

admin.site.register(Product)
admin.site.register(Card)
admin.site.register(ItemCard)
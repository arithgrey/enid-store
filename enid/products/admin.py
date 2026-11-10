from django.contrib import admin
from products.models import Product, PaymentMethod

admin.site.register(Product)
admin.site.register(PaymentMethod)

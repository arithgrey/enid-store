import os
import django
from django.utils.text import slugify
from django.core.files import File


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enid.settings")
django.setup()

from faqs.models import Faq
from returns.models import Returns
from products.models import Product
from variants.models import Variant
from product_variant.models import ProductVariant
from categories.models import Category
from state.models import State

class DataLoader:
    def __init__(self, model, data, slug=0):
        self.model = model
        self.data = data
        self.slug = slug

    def load_data(self):
        print(f"Ingresando {self.model}")
        for item in self.data:
            if self.slug:
                slug = slugify(item["name"])
                item["slug"] = slug            
            if not self.model.objects.filter(**item).exists():
                self.model.objects.create(**item)

class FaqsLoader(DataLoader):
    def __init__(self, data):
        super().__init__(Faq, data)

class ReturnsLoader(DataLoader):
    def __init__(self, data):
        super().__init__(Returns, data)

class CategoriesLoader(DataLoader):
    def __init__(self, data,slug=0):
        super().__init__(Category, data, slug)

class VariantLoader(DataLoader):
    def __init__(self, data):
        super().__init__(Variant, data)

class StateLoader(DataLoader):
    def __init__(self, data):
        super().__init__(State, data)

class ProductLoader:
    
   def products(self, data):
    products = []
    for item in data:
        slug = slugify(item["name"])
        item["slug"] = slug

        # Obtener la instancia de Category
        category_id = item["category"]
        category = Category.objects.get(id=category_id)
        item["category"]=category

        # Crear el producto con la instancia de Category
        if not Product.objects.filter(**item).exists():
            product = Product.objects.create(**item) 
            products.append(product)
    
    return products

        

class ProductVariantLoader:

    def load_product_variant(self, product_id, variant_id, pieces):
        print("-------------AGREGANDO PRODUCT VARIANT-----------")
        # Obtener instancias específicas de Product y Variant
        product_instance = Product.objects.get(id=product_id)
        variant_instance = Variant.objects.get(id=variant_id)

        # Verificar si ya existe un ProductVariant con la misma combinación
        existing_product_variant = ProductVariant.objects.filter(
            product=product_instance,
            variant=variant_instance,            

        ).first()

        if not existing_product_variant:
            # Crear un nuevo objeto ProductVariant solo si no existe
            new_product_variant = ProductVariant.objects.create(
                product=product_instance,
                variant=variant_instance,
                pieces=pieces
            )
            return new_product_variant

        return existing_product_variant


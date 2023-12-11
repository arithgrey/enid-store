import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enid.settings")
django.setup()

from faqs.models import Faq
from returns.models import Returns
from products.models import Product
from variants.models import Variant
from product_variant.models import ProductVariant

class DataLoader:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def load_data(self):
        for item in self.data:
            if not self.model.objects.filter(**item).exists():
                self.model.objects.create(**item)

class FaqsLoader(DataLoader):
    def __init__(self, data):
        super().__init__(Faq, data)

class ReturnsLoader(DataLoader):
    def __init__(self, data):
        super().__init__(Returns, data)

class ProductsLoader(DataLoader):
    def __init__(self, data):
        super().__init__(Product, data)

class VariantLoader(DataLoader):
    def __init__(self, data):
        super().__init__(Variant, data)



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
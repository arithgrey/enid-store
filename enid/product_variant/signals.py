import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from products.models import Product
from variants.models import Variant
from product_variant.models import ProductVariant
from decouple import config

DATA_MODULES = {
    0: 'product_variant.gym_variants',
    1: 'product_variant.clothes_variants',
    # Agrega más si es necesario
}
@receiver(post_migrate)
def create_base_returns(sender, **kwargs):
    if not config('DJANGO_RUNNING_MIGRATIONS', default=False, cast=bool):
        return
    
    if sender.name != 'product_variant':
        return

    
    store = config('STORE',default=0, cast=int)
    module_path = DATA_MODULES.get(store, 'product_variant.gym_variants')  
              
    try:
        data_module = __import__(module_path, fromlist=['data'])
        data = data_module.data
    except ImportError as e:
        print(f"Error al importar el módulo de datos: {e}")
        return
              

    for entry in data:
        product_id = entry.get('product_id')
        variant_id = entry.get('variant_id')
        pieces = entry.get('pieces', 1)  # Valor por defecto si no se proporciona

        load_product_variant(product_id=product_id, variant_id=variant_id, pieces=pieces)


def load_product_variant(product_id, variant_id, pieces):
    
    # Obtener instancias específicas de Product y Variant
    product_instance = Product.objects.get(id=product_id)
    variant_instance = Variant.objects.get(id=variant_id)

    # Verificar si ya existe un ProductVariant con la misma combinación
    existing_product_variant = ProductVariant.objects.filter(
        product=product_instance,
        variant=variant_instance,            

    ).first()

    if not existing_product_variant:
        print("-------------AGREGANDO PRODUCT VARIANT-----------")
        # Crear un nuevo objeto ProductVariant solo si no existe
        new_product_variant = ProductVariant.objects.create(
            product=product_instance,
            variant=variant_instance,
            pieces=pieces                
        )
        return new_product_variant

    return existing_product_variant
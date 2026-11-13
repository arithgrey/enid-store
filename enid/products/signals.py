import os
import logging
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from products.models import Product
from django.utils.text import slugify
from categories.models import Category
from product_group.models import ProductGroup
from initial_products_images import ImagesLoader
from decouple import config

logger = logging.getLogger(__name__)

DATA_MODULES = {
    0: 'products.gym_equipment',
    1: 'products.clothes',
    # Agrega más si es necesario
}

@receiver(post_migrate)
def create_products(sender, **kwargs):
    if not config('DJANGO_RUNNING_MIGRATIONS', default=False, cast=bool):
        return

    if sender.name != 'products':
        return
            
    store = config('STORE',default=0, cast=int)
    module_path = DATA_MODULES.get(store, 'products.gym_equipment')  
                
    try:
        data_module = __import__(module_path, fromlist=['data'])
        data = data_module.data
    except ImportError as e:
        print(f"Error al importar el módulo de datos: {e}")
        return
                
    list_product = []

    for item in data:
        slug = slugify(item["name"])
        item["slug"] = slug

        category_id = item["category"]
        category = Category.objects.get(id=category_id)
        item["category"] = category
        
        if "product_group" in item:
            product_group_id = item["product_group"]
            product_group = ProductGroup.objects.get(id=product_group_id)
            item["product_group"] = product_group

                
        product_id = item["id"]
        product_exists = Product.objects.filter(id=product_id).exists()

        if not product_exists:
            product = Product.objects.create(**item)                
            print(f"Producto creado: {product.name}")           
            list_product.append(product)
                
    images = ImagesLoader()
    images.load_products_images(list_product)

# ---------------------------------------------------------------------------
# Máquina de certificación: promoción automática published -> candidate
# al detectar una orden con ingreso real (status in RECIBIDOS).
# ---------------------------------------------------------------------------
from order.models import Order
from item_order.models import ItemOrder
from products.services import promote_products_to_candidate


@receiver(post_save, sender=Order)
def _promote_on_order_save(sender, instance, **kwargs):
    try:
        promote_products_to_candidate(instance)
    except Exception:
        # No romper el guardado de la orden. Sin PII: solo el pk.
        logger.error("Fallo promoviendo productos a candidate (order=%s)", instance.pk)


@receiver(post_save, sender=ItemOrder)
def _promote_on_item_order_save(sender, instance, **kwargs):
    try:
        promote_products_to_candidate(instance.order)
    except Exception:
        logger.error("Fallo promoviendo productos a candidate (item_order=%s)", instance.pk)

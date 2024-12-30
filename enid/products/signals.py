import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from products.models import Product
from django.utils.text import slugify
from categories.models import Category
from product_group.models import ProductGroup
from initial_products_images import ImagesLoader
from decouple import config

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
        item["category"]=category
        
        if "product_group" in item:
            product_group_id = item["product_group"]
            product_group =  ProductGroup.objects.get(id=product_group_id)
            item["product_group"]=product_group

                
        product_id = item["id"]
        product_exists = Product.objects.filter(id=product_id).exists()

        if not product_exists:
            product = Product.objects.create(**item)                
            print(f"Producto creado: {product.name}")           
            list_product.append(product)
                
    images = ImagesLoader()
    images.load_products_images(list_product)
import os
from django.db.models.signals import post_migrate
from decouple import config
from django.dispatch import receiver
from categories.models import Category

DATA_MODULES = {
    0: 'categories.gym',
    1: 'categories.clothes',
    # Agrega más si es necesario
}

@receiver(post_migrate)
def create_categories(sender, **kwargs):
    
    if not config('DJANGO_RUNNING_MIGRATIONS', default=False, cast=bool):
        return
    
    if sender.name != 'categories':
        return
    
    store = config('STORE',default=0, cast=int)
    module_path = DATA_MODULES.get(store, 'categories.gym')  
              
    try:
        data_module = __import__(module_path, fromlist=['data'])
        data = data_module.data
    except ImportError as e:
        print(f"Error al importar el módulo de datos: {e}")
        return
         
    for item in data:
        Category.objects.get_or_create(**item)
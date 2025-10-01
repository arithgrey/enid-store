import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from products.models import Product
from .models import ProductComponent
from decouple import config

DATA_MODULES = {
    0: 'primary_components.gym_kits'
    # Agrega más si es necesario
}
@receiver(post_migrate)
def create_primary_components(sender, **kwargs):
   
    if not config('DJANGO_RUNNING_MIGRATIONS', default=False, cast=bool):
        return

    if sender.name != 'primary_components':
        return
             
    store = config('STORE',default=0, cast=int)
    module_path = DATA_MODULES.get(store, 'products.gym_equipment')  
                
    try:
        data_module = __import__(module_path, fromlist=['data'])
        data = data_module.data
    except ImportError as e:
        print(f"Error al importar el módulo de datos: {e}")
        return
    
    for item in data:
        kit_id = item['kit']
        components = item['primary_components']
        
        kit = Product.objects.get(id=kit_id)
        print("-------------AGREGANDO COMPONENTES PRIMARIOS -----------")

        for component in components:
            component_id = component['id']
            quantity = component['quantity']
            
            component_product = Product.objects.get(id=component_id)
            ProductComponent.objects.get_or_create(
                kit=kit,
                component=component_product,
                defaults={'quantity': quantity}
            )
            print(f"Componente primario creado/verificado para: {kit.name}")
                
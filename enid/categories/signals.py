import os
from django.db.models.signals import post_migrate
from decouple import config
from django.dispatch import receiver
from categories.models import Category
from store.models import Store

@receiver(post_migrate)
def create_categories(sender, **kwargs):
    
    if config('DJANGO_RUNNING_MIGRATIONS',default=False, cast=bool):        
        if sender.name == "categories":
            store = Store.objects.first()
            if not store:
                print("- Falta ingresar tiendas a DB")
                return
            
            data = [            
                {"id":1,"name": 'Pesas y barras', "store":store},            
                {"id":2,"name": 'Calistenia', "store":store},             
                {"id":3,"name": 'Accesorios', "store":store},                                                        
            ]
            for item in data:

                Category.objects.get_or_create(**item)

            



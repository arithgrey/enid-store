import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from store.models import Store
from django.contrib.auth.models import Group
from decouple import config

@receiver(post_migrate)
def create_stors(sender, **kargs):
    if config('DJANGO_RUNNING_MIGRATIONS',default=False, cast=bool):
        if sender.name == "store":        
            data = [
                {"id":1, "name":"Enid Service"},
                {"id":2, "name":"RIMO"},
                {"id":3, "name":"Carpas reforzadas"},
                ]
            
            for item in data:
                Store.objects.get_or_create(**item)

            Group.objects.get_or_create(name="admin")
            Group.objects.get_or_create(name="ecommerce")
import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from store.models import Store
from django.contrib.auth.models import Group

@receiver(post_migrate)
def create_stors(sender, **kargs):
    if os.environ.get('DJANGO_RUNNING_MIGRATIONS') == 'true':
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
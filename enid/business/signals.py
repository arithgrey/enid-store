import os
from django.db.models.signals import post_migrate
from decouple import config
from django.dispatch import receiver
from business.models import Business

@receiver(post_migrate)
def create_business(sender, **kwargs):
    if config('DJANGO_RUNNING_MIGRATIONS',default=False, cast=bool):
        if sender.name == 'business':                  
            data = [
                {"name":"Enid Service"}
            ]
            for item in data:            
                Business.objects.get_or_create(**item)    

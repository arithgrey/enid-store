import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from business.models import Business

@receiver(post_migrate)
def create_business(sender, **kwargs):
    if os.environ.get('DJANGO_RUNNING_MIGRATIONS') == 'true':
        if sender.name == 'business':                  
            data = [
                {"name":"Enid Service"}
            ]
            for item in data:            
                Business.objects.get_or_create(**item)    

import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from lead_type.models import LeadType
from decouple import config

@receiver(post_migrate)
def create_lead_types(sender, **kwargs):
    
    if config('DJANGO_RUNNING_MIGRATIONS',default=False, cast=bool):
        if sender.name == 'lead_type':        
            lead_types_data = [
                {'id': 1, 'name': 'Al hacer seguir en contacto'},
                {'id': 2, 'name': 'Al registrar orden'},
                {'id': 3, 'name': 'Al hacer registro'},
            ]
            for lead_type_data in lead_types_data:
                
                lead_type_id = lead_type_data['id']
                lead_type_name = lead_type_data['name']
                
                LeadType.objects.get_or_create(
                    id=lead_type_id, defaults={'name': lead_type_name})
                        


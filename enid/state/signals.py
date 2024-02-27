import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from state.models import State
from decouple import config

@receiver(post_migrate)
def create_states(sender, **kwargs):
    if config('DJANGO_RUNNING_MIGRATIONS',default=False, cast=bool):
        if sender.name == 'state':            
            data = [
                {"name":"Aguascalientes"},
                {"name":"Baja California"},
                {"name":"Baja California Sur"},
                {"name":"Campeche"},
                {"name":"Chiapas"},
                {"name":"Chihuahua"},
                {"name": "Ciudad de México"},
                {"name":"Coahuila"},
                {"name":"Colima"},
                {"name":"Durango"},
                {"name":"Estado de México"},
                {"name":"Guanajuato"},
                {"name":"Guerrero"},
                {"name":"Hidalgo"},
                {"name":"Jalisco"},
                {"name":"Michoacán"},
                {"name":"Morelos"},
                {"name":"Nayarit"},
                {"name":"Nuevo León"},
                {"name":"Oaxaca"},
                {"name":"Puebla"},
                {"name":"Querétaro"},
                {"name":"Quintana Roo"},
                {"name":"San Luis Potosí"},
                {"name":"Sinaloa"},
                {"name":"Sonora"},
                {"name":"Tabasco"},
                {"name":"Tamaulipas"},
                {"name":"Tlaxcala"},
                {"name":"Veracruz"},
                {"name":"Yucatán"},
                {"name":"Zacatecas"}
            ]
            for item in data:            
                State.objects.get_or_create(**item)
            
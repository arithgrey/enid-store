import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from returns.models import Returns
from decouple import config

@receiver(post_migrate)
def create_base_returns(sender, **kwargs):
    if config('DJANGO_RUNNING_MIGRATIONS',default=False, cast=bool):
        if sender.name == "returns":
            
            data = [
                {
                    "ask": "¿Cómo es el proceso de devolución de un pedido?",                 
                    "short_answer": "Recuerda que cuentas con 15 días a partir de la entrega de tu pedido para iniciar un proceso de devolución.",
                    "call_to_action":"Checa los pasos aquí"
                },            
                {
                    "ask": "¿Cuánto tardará en llegar mi pedido?",                
                    "short_answer": "- En Ciudad de México, ¡recibe tu pedido el mismo día!, en los estados, el tiempo de entrega es de uno a dos días hábiles",
                    "call_to_action":"Rastrea aquí tu equipo!",
                    "path_seccion":"rastreo"
                }                                             
            ]
            for item in data:            
                Returns.objects.get_or_create(**item)

        
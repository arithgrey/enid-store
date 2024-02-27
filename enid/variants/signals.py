import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from variants.models import Variant
from decouple import config

@receiver(post_migrate)
def create_variants(sender, **kwargs):
    if config('DJANGO_RUNNING_MIGRATIONS',default=False, cast=bool):
        if sender.name == 'variants':     
            
            data = [
                {
                    "id":1,
                    "name": '''Disco de 5KG''',                                 
                    "weight": 5,
                    "disc": True,
                },
                {
                    "id":2,
                    "name": '''Disco de 3KG''',                                 
                    "weight": 3, 
                    "disc": True,               
                },
                {
                    "id":3,
                    "name": '''Disco de 2KG''',                                 
                    "weight": 2, 
                    "disc": True,               
                },
                {
                    "id":4,
                    "name": '''Disco de 1KG''',                                 
                    "weight": 1, 
                    "disc": True,               
                },
                {
                    "id":5,
                    "name": '''Barra Z''',                                 
                    "weight": 1,                
                    "long": 140,
                },
                {
                    "id":6,
                    "name": '''Barra Romana 1kg''',                                 
                    "weight": 1,                
                    "long": 140,
                },
                {
                    "id":7,
                    "name": '''Barra Recta''',                                 
                    "weight": 1.5,                
                    "long": 165,
                },
                {
                    "id":8,
                    "name": '''Maneral para mancuerna''',
                    "weight": .5,                
                    "long": 30,                
                },
                {
                    "id":9,
                    "name": '''Seguro (collarin para ajustar los disos) ''',
                    "weight": .2                
                },
                {
                    "id":10,
                    "name": '''Disco de 3KG''',                                 
                    "weight": 3, 
                    "disc": True,               
                    "material":'Acero'
                },
                {
                    "id":11,
                    "name": '''Disco de 2KG''',                                 
                    "weight": 2, 
                    "disc": True,     
                    "material":'Acero'          
                },
                {
                    "id":12,
                    "name": '''+ seguros adicionales de regalo''',
                    "weight": .2

                },
                {
                    "id":13,
                    "name": '''Barra para calistenia '''                                
                },
                {
                    "id":14,
                    "name": ''' Gancho para box '''                                
                },
                {
                    "id":15,
                    "name": '''Taquetes expansivos '''                                
                },
                {
                    "id":16,
                    "name": '''Disco de 5KG''',                                 
                    "weight": 5, 
                    "disc": True,               
                    "material":'Acero'
                },                                                        
                {
                    "id":17,
                    "name": '''Disco de 10KG''',                                 
                    "weight": 10, 
                    "disc": True,               
                    "material":'Acero'
                },
                {
                    "id":18,
                    "name": '''Disco de 1KG''',                                 
                    "weight": 1, 
                    "disc": True,               
                    "material":'Acero'
                },
                {
                    "id":19,
                    "name": '''Disco de 4KG''',                                 
                    "weight": 4, 
                    "disc": True,               
                    "material":'Acero'
                }, 
                {
                    "id":20,
                    "name": '''Disco de .5KG''',                                 
                    "weight": .5, 
                    "disc": True,               
                    "material":'Acero'
                },
                {
                    "id":21,
                    "name": '''Seguro (collarin para ajustar los disos, acero) ''',
                    "weight": .3                
                },  
                                                
            ]
            for item in data:            
                Variant.objects.get_or_create(**item)
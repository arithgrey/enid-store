from django.db.models.signals import post_migrate
from django.dispatch import receiver
from product_group.models import ProductGroup

@receiver(post_migrate)
def create_states(sender, **kwargs):

    if sender.name == 'product_group':    
        data = [
            {
                "id":1,
                "name": '''Kit de pesas con barra z, recta y mancuernas''',
                "category":"Pesos disponibles",
            },                                   
            {
                "id":2,
                "name": '''Kit de pesas con barra z, Romana, recta y mancuernas''',
                "category":"Pesos disponibles",
            },  
            {
                "id":3,
                "name": '''Solo mancuernas''',
                "category":"Peso del par",
            },                                   
        ]
        
        for item in data:            
            ProductGroup.objects.get_or_create(**item)
        
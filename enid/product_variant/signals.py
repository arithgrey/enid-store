import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from products.models import Product
from variants.models import Variant
from product_variant.models import ProductVariant

@receiver(post_migrate)
def create_base_returns(sender, **kwargs):
    if os.environ.get('DJANGO_RUNNING_MIGRATIONS') == 'true':
        if sender.name == "product_variant":
            
            #34Kg
            load_product_variant(product_id=1, variant_id=1,pieces=2)
            load_product_variant(product_id=1, variant_id=2,pieces=2)
            load_product_variant(product_id=1, variant_id=3,pieces=6)
            load_product_variant(product_id=1, variant_id=4,pieces=6)

            load_product_variant(product_id=1, variant_id=8,pieces=2)
            load_product_variant(product_id=1, variant_id=7,pieces=1)
            load_product_variant(product_id=1, variant_id=5,pieces=1)
            load_product_variant(product_id=1, variant_id=9,pieces=6)

            #42Kg z,recta, mancuernas
            load_product_variant(product_id=9, variant_id=1,pieces=2)
            load_product_variant(product_id=9, variant_id=2,pieces=6)    
            load_product_variant(product_id=9, variant_id=3,pieces=6)
            load_product_variant(product_id=9, variant_id=4,pieces=2)

            load_product_variant(product_id=9, variant_id=8,pieces=2)
            load_product_variant(product_id=9, variant_id=7,pieces=1)
            load_product_variant(product_id=9, variant_id=5,pieces=1)
            load_product_variant(product_id=9, variant_id=9,pieces=6)

            #50Kg z,recta, mancuernas
            load_product_variant(product_id=10, variant_id=1,pieces=2)
            load_product_variant(product_id=10, variant_id=2,pieces=8)    
            load_product_variant(product_id=10, variant_id=3,pieces=8)        

            load_product_variant(product_id=10, variant_id=8,pieces=2)
            load_product_variant(product_id=10, variant_id=7,pieces=1)
            load_product_variant(product_id=10, variant_id=5,pieces=1)
            load_product_variant(product_id=10, variant_id=9,pieces=6)


            #42Kg 2100 

            load_product_variant(product_id=4, variant_id=1,pieces=2)
            load_product_variant(product_id=4, variant_id=2,pieces=6)
            load_product_variant(product_id=4, variant_id=3,pieces=6)
            load_product_variant(product_id=4, variant_id=4,pieces=2)

            load_product_variant(product_id=4, variant_id=8,pieces=2)
            load_product_variant(product_id=4, variant_id=7,pieces=1)
            load_product_variant(product_id=4, variant_id=5,pieces=1)
            load_product_variant(product_id=4, variant_id=6,pieces=1)
            load_product_variant(product_id=4, variant_id=9,pieces=6)    

            #80Kg 3300

            load_product_variant(product_id=5, variant_id=1,pieces=4)
            load_product_variant(product_id=5, variant_id=2,pieces=8)
            load_product_variant(product_id=5, variant_id=3,pieces=12)
            load_product_variant(product_id=5, variant_id=4,pieces=12)

            load_product_variant(product_id=5, variant_id=8,pieces=2)

            load_product_variant(product_id=5, variant_id=7,pieces=1)
            load_product_variant(product_id=5, variant_id=5,pieces=1)
            load_product_variant(product_id=5, variant_id=6,pieces=1)
            load_product_variant(product_id=5, variant_id=9,pieces=10)    
            
            #par de 10kg acero

            load_product_variant(product_id=6, variant_id=10,pieces=4)    
            load_product_variant(product_id=6, variant_id=11,pieces=4)    
            load_product_variant(product_id=6, variant_id=9,pieces=4) 
            load_product_variant(product_id=6, variant_id=12,pieces=2)    
            load_product_variant(product_id=6, variant_id=8,pieces=2)    
            
            #Barras calistenia

            load_product_variant(product_id=7, variant_id=13,pieces=1)
            load_product_variant(product_id=7, variant_id=14,pieces=1)
            load_product_variant(product_id=7, variant_id=15,pieces=8)
            
            #KIT 52 kg acero        
            load_product_variant(product_id=8, variant_id=16,pieces=2)
            load_product_variant(product_id=8, variant_id=19,pieces=4)
            load_product_variant(product_id=8, variant_id=10,pieces=4)                
            load_product_variant(product_id=8, variant_id=11,pieces=4)        
            load_product_variant(product_id=8, variant_id=18,pieces=4)
            load_product_variant(product_id=8, variant_id=20,pieces=4)

            load_product_variant(product_id=8, variant_id=5,pieces=1)
            load_product_variant(product_id=8, variant_id=7,pieces=1)
            load_product_variant(product_id=8, variant_id=6,pieces=1)
            load_product_variant(product_id=8, variant_id=8,pieces=2)        
            load_product_variant(product_id=8, variant_id=21,pieces=10)

            #par 10kg 
            
            load_product_variant(product_id=16, variant_id=2,pieces=4)    
            load_product_variant(product_id=16, variant_id=3,pieces=4)        
            load_product_variant(product_id=16, variant_id=8,pieces=2)
            load_product_variant(product_id=16, variant_id=9,pieces=4)
            
            #par 6kg         
            load_product_variant(product_id=18, variant_id=4,pieces=4)    
            load_product_variant(product_id=18, variant_id=3,pieces=4)        
            load_product_variant(product_id=18, variant_id=8,pieces=2)
            load_product_variant(product_id=18, variant_id=9,pieces=4)
            
            #par 8kg         
            
            load_product_variant(product_id=19, variant_id=3,pieces=8)        
            load_product_variant(product_id=19, variant_id=8,pieces=2)
            load_product_variant(product_id=19, variant_id=9,pieces=4)

            #par 4kg         
            
            load_product_variant(product_id=20, variant_id=4,pieces=8)        
            load_product_variant(product_id=20, variant_id=8,pieces=2)
            load_product_variant(product_id=20, variant_id=9,pieces=4)


            #42Kg recta, mancuernas
            load_product_variant(product_id=17, variant_id=1,pieces=2)
            load_product_variant(product_id=17, variant_id=2,pieces=6)    
            load_product_variant(product_id=17, variant_id=3,pieces=6)
            load_product_variant(product_id=17, variant_id=4,pieces=2)

            load_product_variant(product_id=17, variant_id=8,pieces=2)
            load_product_variant(product_id=17, variant_id=7,pieces=1)        
            load_product_variant(product_id=17, variant_id=9,pieces=6)
            

def load_product_variant(product_id, variant_id, pieces):
    
    # Obtener instancias específicas de Product y Variant
    product_instance = Product.objects.get(id=product_id)
    variant_instance = Variant.objects.get(id=variant_id)

    # Verificar si ya existe un ProductVariant con la misma combinación
    existing_product_variant = ProductVariant.objects.filter(
        product=product_instance,
        variant=variant_instance,            

    ).first()

    if not existing_product_variant:
        print("-------------AGREGANDO PRODUCT VARIANT-----------")
        # Crear un nuevo objeto ProductVariant solo si no existe
        new_product_variant = ProductVariant.objects.create(
            product=product_instance,
            variant=variant_instance,
            pieces=pieces                
        )
        return new_product_variant

    return existing_product_variant
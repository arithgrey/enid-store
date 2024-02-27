import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from products.models import Product
from django.utils.text import slugify
from categories.models import Category
from product_group.models import ProductGroup
from store.models import Store
from initial_products_images import ImagesLoader
from decouple import config

@receiver(post_migrate)
def create_products(sender, **kwargs):
    if config('DJANGO_RUNNING_MIGRATIONS',default=False, cast=bool):
        if sender.name == 'products':                  
            
            data = [
                {
                    "id":1,
                    "name": '''PARA LOS QUE VAN INICIANDO''', 
                    "specific_name":"KIT DE PESAS 16 DISCOS 34KG EN TOTAL, BARRA Z, BARRA RECTA Y MANCUERNAS | ENVÍO GRATIS",
                    "price": 1699,                
                    "weight": 34,
                    "count_discs": True,
                    "top_seller": True,
                    "category": 1,
                    "product_group":1,
                    "name_product_group":"34KG con 16 Discos",                
                    "store_id":1,
                },            
                {
                    "id":3,
                    "name": '''PARA LOS QUE VAN RÁPIDO ''',                 
                    "specific_name":"SOPORTE DE INMERSIóN PARA ENTRENAMIENTO FíSICO, BARRA DE INMERSIóN | ENVÍO GRATIS",
                    "price": 1499,                
                    "weight": 10,
                    "top_seller": True,
                    "category":2,
                    "store_id":1,
                },
                {
                    "id":4,
                    "name": '''PARA QUIEN QUIERE TODO, SIN ESPACIO''',                 
                    "specific_name":"KIT 16 DISCOS 42KG EN TOTAL MANCUERNAS, BARRA RECTA, BARRA Z BARRA ROMANA | ENVÍO GRATIS",
                    "price": 2100,                
                    "weight": 42,
                    "count_discs": True,
                    "top_seller": True,
                    "category":1,
                    "product_group":2,
                    "name_product_group":"42KG con 16 Discos",
                    "store_id":1,
                },            
                {
                    "id":5,
                    "name": '''PARA LOS QUE YA NO VAN AL GYM ''',                 
                    "specific_name":"KIT 80KG MANCUERNAS, BARRA ROMANA, BARRA Z, BARRA RECTA | ENVíO GRATIS",
                    "price": 3300,                
                    "weight": 80,
                    "count_discs": True,
                    "top_seller": True,
                    "category":1,
                    "product_group":2,
                    "name_product_group":"80KG con 28 Discos",
                    "store_id":1,
                },
                {
                    "id":6,
                    "name": '''PARA LOS QUE SOLO OCUPAN MANCUERNAS''',                 
                    "specific_name":"PAR DE MANCUERNAS DE ACERO CON 10KG CADA UNA PESO TOTAL 20KG",
                    "price": 1450,                
                    "weight": 20,
                    "count_discs": True,
                    "top_seller": True,
                    "category":1,
                    "store_id":1,
                },
                {
                    "id":7,
                    "name": '''PARA LOS QUE HACEN CALISTENIA''',  
                    "specific_name":"BARRAS 8 EN 1 SUPER REFORZADAS ENVÍO GRATIS",
                    "price": 1499,                                
                    "top_seller": True,
                    "category":2,
                    "store_id":1,
                },             
                {
                    "id":8,
                    "name": '''PARA QUIEN QUIERE LO NECESARIO, SIN ESPACIO''',
                    "specific_name":"KIT DE PESAS CON 52KG DISCOS DE ACERO PARA PASAR AL SIGUIENTE NIVEL | ENVíO GRATIS",
                    "price": 3800,                                
                    "weight": 52,
                    "top_seller": True,
                    "category":1,
                    "store_id":1,
                },  
                {
                    "id":9,
                    "name": '''PARA LOS QUE VAN INICIANDO 42kg''', 
                    "specific_name":"KIT DE PESAS 16 DISCOS 42KG EN TOTAL, BARRA Z, BARRA RECTA Y MANCUERNAS | ENVÍO GRATIS",
                    "price": 1850,                
                    "weight": 42,
                    "count_discs": True,
                    "top_seller": False,
                    "category": 1,
                    "product_group":1,
                    "name_product_group":"42KG con 16 Discos",
                    "store_id":1,
                },                
                {
                    "id":10,
                    "name": '''PARA LOS QUE VAN INICIANDO 50kg''', 
                    "specific_name":"KIT DE PESAS 20 DISCOS 50KG EN TOTAL, BARRA Z, BARRA RECTA Y MANCUERNAS | ENVÍO GRATIS",
                    "price": 2100,                
                    "weight": 50,
                    "count_discs": True,
                    "top_seller": False,
                    "category": 1,
                    "product_group":1,
                    "name_product_group":"50KG con 20 Discos",
                    "store_id":1,
                },     
                {
                    "id":11,
                    "name": '''PARA LOS QUE DISFRUTAN DE INTERCAMBIAR PESOS''', 
                    "specific_name":"KIT DE 2 SEGUROS PARA BARRAS Y MANCUERNAS STANDARD DE UNA PULGADA, DE METAL, PARA EL INTERCAMBIO RÁPIDO Y PRÁCTICO DE DISCOS | ENVÍO GRATIS",
                    "price": 169,                
                    "weight": .5,
                    "count_discs": False,
                    "top_seller": False,
                    "category": 3,
                    "store_id":1,
                },   
                {
                    "id":12,
                    "name": '''PARA LOS QUE QUIEREN HACER REMO CON PESAS''', 
                    "specific_name":"BARRA ROMANA ESTÁNDAR DE UNA PULGADA 15KG ACERO BLACK | ENVÍO GRATIS",
                    "price": 999,                
                    "weight": 15,
                    "count_discs": False,
                    "top_seller": False,
                    "category": 3,                               
                    "store_id":1,
                },     
                {
                    "id":13,
                    "name": '''PARA LOS QUE QUIEREN HACER EL PREDICADOR EN CASA''', 
                    "specific_name":"BARRA Z SOLIDA DE ACERO CON SEGUROS, 12KG EN TOTAL SOPORTA 350KG PARA DISCOS DE UNA PULGADA ESTáNDAR | ENVíO GRATIS",
                    "price": 999,                
                    "weight": 12,
                    "count_discs": False,
                    "top_seller": False,
                    "category": 3,                               
                    "store_id":1,
                },     
                {
                    "id":14,
                    "name": '''PARA LOS QUE QUIEREN HACER EL PREDICADOR EN CASA SIN EXCEDERSE''', 
                    "specific_name":"BARRA Z CON 2 SEGUROS PARA DISCOS STANDARD DE UNA PULGADA, SOPORTA 60KG | ENVÍO GRATIS",
                    "price": 499,                
                    "weight": 1,
                    "count_discs": False,
                    "top_seller": False,
                    "category": 3,
                    "store_id":1,
                },     
                {
                    "id":15,
                    "name": '''PARA LOS QUE QUIEREN HACER REMO CON PESAS SIN EXCEDERSE''', 
                    "specific_name":"BARRA Z CON 2 SEGUROS PARA DISCOS STANDARD DE UNA PULGADA, SOPORTA 60KG | ENVÍO GRATIS",
                    "price": 499,                
                    "weight": 1,
                    "count_discs": False,
                    "top_seller": False,
                    "category": 3,                       
                    "store_id":1,
                },     
                {
                    "id":16,
                    "name": '''PARA LOS QUE SOLO OCUPAN MANCUERNAS''', 
                    "specific_name":"PAR DE MANCUERNAS DE 10KG EN TOTAL 20 KG SON 2 PIEZAS | ENVíO GRATIS",
                    "price": 899,
                    "weight": 20,
                    "count_discs": True,
                    "top_seller": False,
                    "category": 1,         
                    "product_group":3,
                    "name_product_group":"10Kg C/U total 20kg",
                    "store_id":1,
                },     
                {
                    "id":17,
                    "name": '''PARA LOS QUE OCUPAN MANCUERNAS y BARRA''', 
                    "specific_name":"BARRA 22KG + PAR MANCUERNAS 10KG EN TOTAL 42KG A DOMICILIO PAGAS A TU ENTREGA 16 DISCOS | ENVíO GRATIS",
                    "price": 1700,                
                    "weight": 42,
                    "count_discs": True,
                    "top_seller": False,
                    "category": 1,
                    "store_id":1,
                },     
                {
                    "id":18,
                    "name": '''PARA LOS QUE SOLO OCUPAN MANCUERNAS''', 
                    "specific_name":"PAR DE MANCUERNAS DE 6KG EN TOTAL 12 KG SON 2 PIEZAS | ENVíO GRATIS",
                    "price": 750,                
                    "weight": 12,
                    "count_discs": True,
                    "top_seller": True,
                    "category": 1,         
                    "product_group":3,
                    "name_product_group":"6Kg C/U total 12kg",
                    "store_id":1,
                },     
                {
                    "id":19,
                    "name": '''PARA LOS QUE SOLO OCUPAN MANCUERNAS''', 
                    "specific_name":"PAR DE MANCUERNAS DE 8KG EN TOTAL 16 KG SON 2 PIEZAS | ENVíO GRATIS",
                    "price": 799,                
                    "weight": 16,
                    "count_discs": True,
                    "top_seller": False,
                    "category": 1,         
                    "product_group":3,
                    "name_product_group":"8Kg C/U total 16kg",
                    "store_id":1,
                },     
                {
                    "id":20,
                    "name": '''PARA LOS QUE SOLO OCUPAN MANCUERNAS''', 
                    "specific_name":"PAR DE MANCUERNAS DE 4KG EN TOTAL 8 KG SON 2 PIEZAS | ENVíO GRATIS",
                    "price": 530,                
                    "weight": 8,
                    "count_discs": True,
                    "top_seller": False,
                    "category": 1,         
                    "product_group":3,
                    "name_product_group":"4Kg C/U total 8kg",
                    "store_id":1,
                },
                                                
            ]
            
            list_product = []

            for item in data:
                slug = slugify(item["name"])
                item["slug"] = slug

                store_id = item["store_id"]
                item["store"] = Store.objects.get(id=store_id)
                
                category_id = item["category"]
                category = Category.objects.get(id=category_id)
                item["category"]=category
                
                if "product_group" in item:
                    product_group_id = item["product_group"]
                    product_group =  ProductGroup.objects.get(id=product_group_id)
                    item["product_group"]=product_group

                
                product_id = item["id"]
                product_exists = Product.objects.filter(id=product_id).exists()

                if not product_exists:
                    product = Product.objects.create(**item)                
                    print(f"Producto creado: {product.name}")           
                    list_product.append(product)
                
            images = ImagesLoader()
            images.load_products_images(list_product)
        



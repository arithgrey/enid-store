import os
from models_loader import BusinessLoader, FaqsLoader, ReturnsLoader, VariantLoader
from models_loader import ProductVariantLoader,  ProductLoader, CategoriesLoader, StateLoader, ProductGroupLoader
from initial_products_images import ImagesLoader
from initial_business_images import ImagesBusinessLoader
from django.contrib.auth.models import Group

class EnidLoader:

    def load_business(self):

        data = [
            {"name":"Enid Service"},            
        ]
        BusinessLoader(data).load_data()

    def load_states(self):

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
        StateLoader(data).load_data()



    def load_Faqs(self):
        data = [
                
            {"ask": "1.- ¿Carísimas?", 
            "answer": "Na! más bien tienes mente pobre, más caras tus 🍻 chelas que te metes cada semana 😜",         
            "url_img": "https://media.giphy.com/media/XozypzpGakVuX2ciZJ/giphy.gif"
            },

            {"ask": "2.- Lo que escribimos:", "answer": '''✅ Si no te agradan las compras en línea, en CDMX tenemos la capacidad de entregarte y que pagues al recibir tu equipo en tu domicilio''',          
            "url_img": "https://media.giphy.com/media/y9Tia8PxQMlhK/giphy.gif",
            'we_mean':'''Haz tu pedido en línea. Ya es 2023 y sigues con tus pensamientos vieja escuela 👴🏽. En la Ciudad de México no hay bronca, es nuestra propuesta de valor que te las entreguemos en tus manitas 👐🏻 y pagues al recibirlas. Pero en otro estado te las enviamos 🚚. Ni modo que fueras tan especial para visitarte'''
            },

            {"ask": "3.- Esas pesas son muy feas...", 
            "answer": "Bueno pero... ¿no las vas a besar verdad? o ¿si? 😱", 
            "url_img": "https://media.giphy.com/media/71taCLE2Q5lq8/giphy.gif"
            },

            {"ask": "4.- ¿Tienen referencias?", 
            "answer": "Obvio 😎 ¿y tu? 😱😢", 
            "url_img": "https://media.giphy.com/media/iDDBOw59fLjT2o4HBn/giphy.gif"
            },

            {"ask": "5.- ¿De que estan hechas?", 
            "answer": "De oro 💰 para el cliente lo que pida 🫡 estamos a tus órdenes", 
            "url_img": "https://media.giphy.com/media/WsQzhuGMxAuXGqSAcS/giphy-downsized-large.gif"
            },

            {"ask": "6.- ¿Todo Facebook tiene anunciadas esas pesas?", 
            "answer": "Seee ... pero hay mucho estafata robando nuestras fotos para delinquir 🐁🐀, mejor pídelas aquí ó aquí", 
            "url_img": "https://media.giphy.com/media/3oEdv9pgtUVVYdpaY8/giphy.gif"
            },

            {"ask": "¿No le gustaron nuestras FAQ a su señoría? 🤴🫅", 
            "answer": "Disculpe por no usar la hipocresía que se emplea cada que le venden funkibasuras 😎, puede retirarse👋", 
            "url_img": "https://media.giphy.com/media/26ufcVAp3AiJJsrIs/giphy.gif"
            }            
        ]
        FaqsLoader(data).load_data()

    def load_Returns(self):
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
        ReturnsLoader(data).load_data()            

    def load_product_group(self):
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

        ProductGroupLoader(data).load_data()


    def load_categories(self):
        data = [            
            {"id":1,"name": '''Pesas y barras'''},            
            {"id":2,"name": '''Calistenia'''},             
            {"id":3,"name": '''Accesorios'''},                                                        
        ]
        
        loader = CategoriesLoader()
        loader.categories(data)
    
    def load_groups(self):
        Group.objects.get_or_create(name="admin")
        Group.objects.get_or_create(name="ecommerce")


    def load_products(self):
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
            },            
            {
                "id":3,
                "name": '''PARA LOS QUE VAN RÁPIDO ''',                 
                "specific_name":"SOPORTE DE INMERSIóN PARA ENTRENAMIENTO FíSICO, BARRA DE INMERSIóN | ENVÍO GRATIS",
                "price": 1499,                
                "weight": 10,
                "top_seller": True,
                "category":2,
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
            },
            {
                "id":7,
                "name": '''PARA LOS QUE HACEN CALISTENIA''',  
                "specific_name":"BARRAS 8 EN 1 SUPER REFORZADAS ENVÍO GRATIS",
                "price": 1499,                                
                "top_seller": True,
                "category":2,
            },             
            {
                "id":8,
                "name": '''PARA QUIEN QUIERE LO NECESARIO, SIN ESPACIO''',
                "specific_name":"KIT DE PESAS CON 52KG DISCOS DE ACERO PARA PASAR AL SIGUIENTE NIVEL | ENVíO GRATIS",
                "price": 3800,                                
                "weight": 52,
                "top_seller": True,
                "category":1,
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
            },
                                             
        ]
        
        loader = ProductLoader()
        products = loader.products(data)
        
        images_loader = ImagesLoader()
        images_loader.load_products_images(products)
        

    def load_variant(self):
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

        VariantLoader(data).load_data()            


    def load_product_variant(self):

        loader = ProductVariantLoader()
        #34Kg
        loader.load_product_variant(product_id=1, variant_id=1,pieces=2)
        loader.load_product_variant(product_id=1, variant_id=2,pieces=2)
        loader.load_product_variant(product_id=1, variant_id=3,pieces=6)
        loader.load_product_variant(product_id=1, variant_id=4,pieces=6)

        loader.load_product_variant(product_id=1, variant_id=8,pieces=2)
        loader.load_product_variant(product_id=1, variant_id=7,pieces=1)
        loader.load_product_variant(product_id=1, variant_id=5,pieces=1)
        loader.load_product_variant(product_id=1, variant_id=9,pieces=6)

        #42Kg z,recta, mancuernas
        loader.load_product_variant(product_id=9, variant_id=1,pieces=2)
        loader.load_product_variant(product_id=9, variant_id=2,pieces=6)    
        loader.load_product_variant(product_id=9, variant_id=3,pieces=6)
        loader.load_product_variant(product_id=9, variant_id=4,pieces=2)

        loader.load_product_variant(product_id=9, variant_id=8,pieces=2)
        loader.load_product_variant(product_id=9, variant_id=7,pieces=1)
        loader.load_product_variant(product_id=9, variant_id=5,pieces=1)
        loader.load_product_variant(product_id=9, variant_id=9,pieces=6)

        #50Kg z,recta, mancuernas
        loader.load_product_variant(product_id=10, variant_id=1,pieces=2)
        loader.load_product_variant(product_id=10, variant_id=2,pieces=8)    
        loader.load_product_variant(product_id=10, variant_id=3,pieces=8)        

        loader.load_product_variant(product_id=10, variant_id=8,pieces=2)
        loader.load_product_variant(product_id=10, variant_id=7,pieces=1)
        loader.load_product_variant(product_id=10, variant_id=5,pieces=1)
        loader.load_product_variant(product_id=10, variant_id=9,pieces=6)


        #42Kg 2100 

        loader.load_product_variant(product_id=4, variant_id=1,pieces=2)
        loader.load_product_variant(product_id=4, variant_id=2,pieces=6)
        loader.load_product_variant(product_id=4, variant_id=3,pieces=6)
        loader.load_product_variant(product_id=4, variant_id=4,pieces=2)

        loader.load_product_variant(product_id=4, variant_id=8,pieces=2)
        loader.load_product_variant(product_id=4, variant_id=7,pieces=1)
        loader.load_product_variant(product_id=4, variant_id=5,pieces=1)
        loader.load_product_variant(product_id=4, variant_id=6,pieces=1)
        loader.load_product_variant(product_id=4, variant_id=9,pieces=6)    

        #80Kg 3300

        loader.load_product_variant(product_id=5, variant_id=1,pieces=4)
        loader.load_product_variant(product_id=5, variant_id=2,pieces=8)
        loader.load_product_variant(product_id=5, variant_id=3,pieces=12)
        loader.load_product_variant(product_id=5, variant_id=4,pieces=12)

        loader.load_product_variant(product_id=5, variant_id=8,pieces=2)

        loader.load_product_variant(product_id=5, variant_id=7,pieces=1)
        loader.load_product_variant(product_id=5, variant_id=5,pieces=1)
        loader.load_product_variant(product_id=5, variant_id=6,pieces=1)
        loader.load_product_variant(product_id=5, variant_id=9,pieces=10)    
        
        #par de 10kg acero

        loader.load_product_variant(product_id=6, variant_id=10,pieces=4)    
        loader.load_product_variant(product_id=6, variant_id=11,pieces=4)    
        loader.load_product_variant(product_id=6, variant_id=9,pieces=4) 
        loader.load_product_variant(product_id=6, variant_id=12,pieces=2)    
        loader.load_product_variant(product_id=6, variant_id=8,pieces=2)    
        
        #Barras calistenia

        loader.load_product_variant(product_id=7, variant_id=13,pieces=1)
        loader.load_product_variant(product_id=7, variant_id=14,pieces=1)
        loader.load_product_variant(product_id=7, variant_id=15,pieces=8)
        
        #KIT 52 kg acero        
        loader.load_product_variant(product_id=8, variant_id=16,pieces=2)
        loader.load_product_variant(product_id=8, variant_id=19,pieces=4)
        loader.load_product_variant(product_id=8, variant_id=10,pieces=4)                
        loader.load_product_variant(product_id=8, variant_id=11,pieces=4)        
        loader.load_product_variant(product_id=8, variant_id=18,pieces=4)
        loader.load_product_variant(product_id=8, variant_id=20,pieces=4)

        loader.load_product_variant(product_id=8, variant_id=5,pieces=1)
        loader.load_product_variant(product_id=8, variant_id=7,pieces=1)
        loader.load_product_variant(product_id=8, variant_id=6,pieces=1)
        loader.load_product_variant(product_id=8, variant_id=8,pieces=2)        
        loader.load_product_variant(product_id=8, variant_id=21,pieces=10)

        #par 10kg 
        
        loader.load_product_variant(product_id=16, variant_id=2,pieces=4)    
        loader.load_product_variant(product_id=16, variant_id=3,pieces=4)        
        loader.load_product_variant(product_id=16, variant_id=8,pieces=2)
        loader.load_product_variant(product_id=16, variant_id=9,pieces=4)
        
        #par 6kg         
        loader.load_product_variant(product_id=18, variant_id=4,pieces=4)    
        loader.load_product_variant(product_id=18, variant_id=3,pieces=4)        
        loader.load_product_variant(product_id=18, variant_id=8,pieces=2)
        loader.load_product_variant(product_id=18, variant_id=9,pieces=4)
        
        #par 8kg         
         
        loader.load_product_variant(product_id=19, variant_id=3,pieces=8)        
        loader.load_product_variant(product_id=19, variant_id=8,pieces=2)
        loader.load_product_variant(product_id=19, variant_id=9,pieces=4)

        #par 4kg         
         
        loader.load_product_variant(product_id=20, variant_id=4,pieces=8)        
        loader.load_product_variant(product_id=20, variant_id=8,pieces=2)
        loader.load_product_variant(product_id=20, variant_id=9,pieces=4)


        #42Kg recta, mancuernas
        loader.load_product_variant(product_id=17, variant_id=1,pieces=2)
        loader.load_product_variant(product_id=17, variant_id=2,pieces=6)    
        loader.load_product_variant(product_id=17, variant_id=3,pieces=6)
        loader.load_product_variant(product_id=17, variant_id=4,pieces=2)

        loader.load_product_variant(product_id=17, variant_id=8,pieces=2)
        loader.load_product_variant(product_id=17, variant_id=7,pieces=1)        
        loader.load_product_variant(product_id=17, variant_id=9,pieces=6)


    def load_base(self):
        self.load_groups()
        self.load_categories()        
        self.load_product_group()
        self.load_business()
        self.load_states()
        self.load_Faqs()
        self.load_Returns()        
        self.load_products()
        self.load_variant()
        self.load_product_variant()
        image_business = ImagesBusinessLoader()
        image_business.add_business_images()
        
        

if __name__ == "__main__":
    EnidLoader().load_base()            
import os
from models_loader import BusinessLoader, FaqsLoader, ReturnsLoader, VariantLoader
from models_loader import ProductVariantLoader, CategoriesLoader, ProductLoader, StateLoader
from initial_products_images import ImagesLoader
from initial_business_images import ImagesBusinessLoader

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
            },
            

        ]
        FaqsLoader(data).load_data()

    def load_Returns(self):
        data = [
            {
                "ask": "¿Cómo es el proceso de devolución de un pedido?",                 
                "short_answer": '''Recuerda que cuentas con 15 días a partir de la entrega de tu pedido para iniciar un proceso de devolución.''',
                "call_to_action":"Checa los pasos aquí"

            },
            
            {
                "ask": "¿Cuánto tardará en llegar mi pedido?",                
                "short_answer": '''- En Ciudad de México, ¡recibe tu pedido el mismo día!, en los estados, 
                el tiempo de entrega es de uno a dos días hábiles''',
                "call_to_action":"Rastrea aquí tu equipo!",
                "path_seccion":"rastreo"

             },   
                                             
        ]
        ReturnsLoader(data).load_data()            

    def load_categories(self):
        data = [
            {
                "id":1,
                "name": '''Pesas y barras''',
            },            
           {
                "id":2,
                "name": '''Accesorios''',
                
            },             
                                             
        ]
        CategoriesLoader(data,1).load_data()



    def load_products(self):
        data = [
            {
                "id":1,
                "name": '''PARA LOS QUE VAN INICIANDO''',                 
                "price": 1550,                
                "weight": 34,
                "count_discs": True,
                "top_seller": True,
                "category": 1,
            },            
           {
                "id":3,
                "name": '''PARA LOS QUE VAN RÁPIDO ''',                 
                "price": 1499,                
                "weight": 10,
                "top_seller": True,
                "category":1,
            },
            {
                "id":4,
                "name": '''PARA QUIEN QUIERE TODO, SIN ESPACIO''',                 
                "price": 2100,                
                "weight": 42,
                "count_discs": True,
                "top_seller": True,
                "category":1,
            },            
            {
                "id":5,
                "name": '''PARA LOS QUE YA NO VAN AL GYM ''',                 
                "price": 3300,                
                "weight": 80,
                "count_discs": True,
                "top_seller": True,
                "category":1,
            },
            {
                "id":6,
                "name": '''PARA LOS QUE SOLO OCUPAN MANCUERNAS''',                 
                "price": 1450,                
                "weight": 20,
                "count_discs": True,
                "top_seller": True,
                "category":1,
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
        
        #par de 10kg

        loader.load_product_variant(product_id=6, variant_id=10,pieces=4)    
        loader.load_product_variant(product_id=6, variant_id=11,pieces=4)    
        loader.load_product_variant(product_id=6, variant_id=9,pieces=4) 
        loader.load_product_variant(product_id=6, variant_id=12,pieces=2)    
        loader.load_product_variant(product_id=6, variant_id=8,pieces=2)    


    def load_base(self):
        self.load_business()
        self.load_states()
        self.load_Faqs()
        self.load_Returns()
        self.load_categories()
        self.load_products()
        self.load_variant()
        self.load_product_variant()
        image_business = ImagesBusinessLoader()
        image_business.add_business_images()
        

if __name__ == "__main__":
    EnidLoader().load_base()
            
    

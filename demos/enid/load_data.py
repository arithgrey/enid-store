# load_data.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enid.settings")
django.setup()

from faqs.models import Faq

def cargar_datos():
    datos = [
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

    for dato in datos:
        # Comprueba si ya existe una entrada con las mismas características
        existente = Faq.objects.filter(ask=dato["ask"], answer=dato["answer"]).exists()

        # Si no existe, crea la entrada
        if not existente:
            Faq.objects.create(**dato)

if __name__ == "__main__":
    cargar_datos()

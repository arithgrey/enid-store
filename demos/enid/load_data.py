import os
from models_loader import FaqsLoader, ReturnsLoader

class EnidLoader:
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

    def load_base(self):
        self.load_Faqs()
        self.load_Returns()

if __name__ == "__main__":
    EnidLoader().load_base()

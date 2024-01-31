import os
import django
from django.core.files import File
from image.models import Image 
from initial_images import Images
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enid.settings")
django.setup()

class ImagesLoader(Images):            
    
    def load_products_images(self, products):
        base_path = 'initial_images/'
        base = [
            {"id": 6, "path": '10_kg_acero.jpeg','is_main':True},
            {"id": 6, "path": '10_kg_acero_1.jpeg','is_main':False},
            {"id": 6, "path": '10_kg_acero_2.jpeg','is_main':False},
            {"id": 5, "path": 'IMG_80kg_1.jpeg','is_main':True},
            {"id": 5, "path": 'IMG_80kg_2.jpeg','is_main':False},
            {"id": 5, "path": 'IMG_80kg_3.jpeg','is_main':False},
            {"id": 5, "path": 'IMG_80kg_4.jpeg','is_main':False},
            {"id": 4, "path": 'IMG_42kg_1.jpeg','is_main':True},
            {"id": 4, "path": 'IMG_42kg_2.jpeg','is_main':False},
            {"id": 1, "path": 'IMG_34kg_1.jpeg','is_main':True},
            {"id": 1, "path": 'IMG_34kg_1.jpeg','is_main':False},
            {"id": 3, "path": 'barras_parlelas.jpg','is_main':True},
            {"id": 3, "path": 'barras_parlelas_1.jpg','is_main':False},
            {"id": 3, "path": 'barras_parlelas_1.jpg','is_main':False},            
        ]        
        
        for product in products:
            for item in base:
                if product.id == item['id']:
                    image = f"{base_path}{item['path']}"                    
                    imageObject = self.save_image(image, item["path"], item["is_main"])                    
                    if imageObject is not None:
                        product.images.add(imageObject)
                        print(f'Agregando imagen a pruduct {product.id}')
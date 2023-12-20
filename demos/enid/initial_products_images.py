import os
import django
from django.core.files import File
from image.models import Image 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enid.settings")
django.setup()

class ImagesLoader:    
        
    def save_image(self,file_path,file_name,is_main=False):

        path_uploads = f'uploads/{file_name}'
        if os.path.exists(path_uploads):        
            os.remove(path_uploads)

        with open(file_path, 'rb') as file:
            django_file = File(file)        
            image = Image(is_main=is_main)
            image.image.save(os.path.basename(file_path), django_file, save=True)
            return image

    def load_products_images(self, products):
        base_path = 'initial_images/'
        base = [
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
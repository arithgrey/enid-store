import os
import django
from business.models import Business
from initial_images import Images

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enid.settings")
django.setup()

class ImagesBusinessLoader(Images):    
            
    def add_business_images(self):

        base_path = 'initial_images/business/'
        allow_extensions = ['.jpg', '.png', '.jpeg']          
        images = [archivo for archivo in os.listdir(base_path) if any(archivo.endswith(ext) for ext in allow_extensions)]
        
        business = Business.objects.first()

        for item in images:
            image = f"{base_path}{item}"                    
            
            imageObject = self.save_image(image, item)                    
            if imageObject is not None:
                business.images.add(imageObject)
                print(f'Agregando imagen a negocio {business.id}')
            


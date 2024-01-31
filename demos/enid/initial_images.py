import os
import django
from django.core.files import File
from image.models import Image 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enid.settings")
django.setup()

class Images:    
        
    def save_image(self, file_path, file_name, is_main=False):        
        existing_image = Image.objects.filter(image__icontains=file_name).first()

        if existing_image:
            print(f"La imagen con el nombre '{file_name}' ya existe en la base de datos.")
            return None

        path_uploads = f'uploads/{file_name}'
        if os.path.exists(path_uploads):        
            os.remove(path_uploads)

        with open(file_path, 'rb') as file:
            django_file = File(file)        
            image = Image(is_main=is_main)
            image.image.save(file_name, django_file, save=True)
            return image
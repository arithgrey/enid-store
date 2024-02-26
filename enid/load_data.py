from initial_business_images import ImagesBusinessLoader
from django.contrib.auth.models import Group

class EnidLoader:
     
    def load_base(self):        
   
        image_business = ImagesBusinessLoader()
        image_business.add_business_images()        

if __name__ == "__main__":
    EnidLoader().load_base()
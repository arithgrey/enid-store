from initial_images import Images
from decouple import config

DATA_MODULES = {
    0: 'products.gym_imgs',
    1: 'products.clothes_imgs',
    # Agrega más si es necesario
}

class ImagesLoader(Images):                
    
    def load_products_images(self, products):
    
        store = config('STORE',default=0, cast=int)
        module_path = DATA_MODULES.get(store, 'products.gym_imgs')
        
        try:
            data_module = __import__(module_path, fromlist=['data'])
            data = data_module.data
        except ImportError as e:
            print(f"Error al importar el módulo de datos: {e}")
            return
    
        base_path = 'initial_images/'
        for product in products:
            for item in data:
                if product.id == item['id']:
                    image = f"{base_path}{item['path']}"                    
                    imageObject = self.save_image(image, item["path"], item["is_main"])                    
                    if imageObject is not None:
                        product.images.add(imageObject)
                        print(f'Agregando imagen a pruduct {product.id}')
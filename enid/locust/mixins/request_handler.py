import logging

class RequestHandlerMixin:
    def __init__(self):
        # Configurar el logger en el constructor
        self.logger = logging.getLogger(self.__class__.__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    
    def handle_response(self, response):
        if response.status_code != 200:
            self.logger.error(f"Request failed with status code: {response.status_code}")
            self.logger.error(response.text)
        else:
            self.logger.info(f"Request succeeded with status code: {response.status_code}")


    def send_get_request(self, url, **kwargs):
        """Método reutilizable para construir URL, enviar solicitud e imprimir información."""
        self.logger.info("_________________________") 
        self.logger.info(f"Requesting URL: {url}")
        self.logger.info("_________________________") 
        
        response = self.client.get(url)
        self.handle_response(response)
        
    def send_post_request(self, url, data, **kwargs):
        """Método reutilizable para construir URL, enviar solicitud e imprimir información."""
        
        self.logger.info("_________________________") 
        self.logger.info(f"Requesting URL: {url}")
        self.logger.info(f"Payload Enviado: {data}")  # Imprimir el payload aquí también
        self.logger.info("_________________________") 
        
        response = self.client.post(url, json=data, headers={})
        self.logger.info(f"Response status: {response.status_code}")

        self.logger.info("_________________________RESPONSE_________________") 
        self.logger.info(f"Response text: {response}")
        
        # Manejar la respuesta
        self.handle_response(response)
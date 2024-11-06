from locust import HttpUser, TaskSet, task, between
from faker import Faker
import random
from mixins.request_handler import RequestHandlerMixin

class OrderBehavior(HttpUser, RequestHandlerMixin):
    wait_time = between(1, 3)
    fake = Faker()

    def generate_fake_product(self):
        """Genera datos de productos de prueba."""
        return {
            "id": random.randint(1, 10),  # Supón que hay productos con id del 1 al 10
            "price": round(random.uniform(10, 500), 2),
            "quantity": random.randint(1, 5),
        }

    @task
    def create_order(self):
        """Prueba de carga para la creación de órdenes"""
        data = {
            "email": self.fake.email(),
            "name": self.fake.name(),
            "postal_code": self.fake.postcode(),
            "street": self.fake.street_address(),
            "number": self.fake.building_number(),
            "interior_number": self.fake.building_number(),
            "colony": self.fake.city_prefix(),
            "delegation_or_municipality": self.fake.city(),
            "city": self.fake.city(),
            "state": 1,
            "phone_number": self.fake.phone_number(),
            "products": [self.generate_fake_product() for _ in range(random.randint(1, 5))],
            "stripe_token": "tok_fake_visa",
        }
        
        self.send_post_request("/api/orden/compra/", data=data)
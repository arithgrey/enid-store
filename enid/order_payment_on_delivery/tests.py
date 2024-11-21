from share_test.mixin import CommonMixinTest
from django.urls import reverse
from order.models import Order
from rest_framework import status
from share_test.commons import CommonsTest
from state.models import State

class TestPaymentOnDelivery(CommonMixinTest):
    def setUp(self):            
        super().setUp()
        self.commons = CommonsTest()
        state = State.objects.create(id=1,name="CDMX")        
        self.state = state

    def crear_payment_on_delivery_user(self, **kwargs):
        # Instanciar Faker si no está ya configurado
        
        # Generar datos ficticios
        name = self.fake.name()
        street = self.fake.street_address()
        
        # Generar un número telefónico válido para México usando Faker
        phone_number = self.fake.msisdn()  # Número telefónico ficticio
        phone_number = f"+52{phone_number[:10]}"  # Agregar prefijo y truncar a 10 dígitos
        
        # Construir los datos por defecto
        defaults = {
            'name': name,
            'phone_number': phone_number,
            'street': street    
        }
        
        # Combinar con otros datos si se pasan como kwargs
        return {**defaults, **kwargs}

        
    def test_create_order_payment_on_delivery(self):
        user  = self.crear_payment_on_delivery_user()
        
        products = {
            'products': self.commons.create_multiple_fake_products(
                quantity=3,     
                as_dict=True
                )
            }
        
        data = {**user, **products}
        response = self.client.post('/order-payment-on-delivery/pod/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Order.objects.filter(user__email__contains=user['name'].replace(' ', '').lower()).exists())
    
    #Validar que no se permitan ordenes de compra sin productos
    def test_order_creation_without_products(self):
        user = self.crear_payment_on_delivery_user()
        data = {**user, 'products': []}
        response = self.client.post('/order-payment-on-delivery/pod/', data, format='json')

        # Validar errores de validación
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("products", response.json())
    
    #Validar con Datos de Usuario Inválidos
    def test_order_creation_with_invalid_user_data(self):
        products = {
            'products': self.commons.create_multiple_fake_products(
                quantity=2,     
                as_dict=True
            )
        }
        data = {
            'name': '',  # Nombre vacío
            'phone_number': '123',  # Número de teléfono inválido
            'street': 'Calle Falsa 123'
        }
        data.update(products)

        response = self.client.post('/order-payment-on-delivery/pod/', data, format='json')

        # Validar errores de usuario
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.json())
        self.assertIn("phone_number", response.json())
    
    # Prueba de Integridad de Datos        
    def test_data_persistence_on_successful_order(self):
        user = self.crear_payment_on_delivery_user()
        products = {
            'products': self.commons.create_multiple_fake_products(
                quantity=2,     
                as_dict=True
            )
        }
        data = {**user, **products}
        response = self.client.post('/order-payment-on-delivery/pod/', data, format='json')
        
        # Validar persistencia
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        order = Order.objects.get(user__email__contains=user['name'].replace(' ', '').lower())
        self.assertEqual(order.items.count(), len(products['products']))
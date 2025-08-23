from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from order.models import Order
from django.contrib.auth.models import User
from address.models import Address
from products.models import Product
from state.models import State
from django.urls import reverse

class OrderPaymentOnDeliverySourceTestCase(APITestCase):
    
    def setUp(self):
        """Configuración inicial para los tests"""
        # Crear estado por defecto
        self.state, _ = State.objects.get_or_create(id=1, defaults={'name': "Estado Test"})
        
        # Usar producto real que existe en la base de datos de test
        self.product = Product.objects.get(id=1)  # Producto con precio 1600.00
    
    def test_create_order_with_source(self):
        """Test crear orden con campo source válido"""
        data = {
            'name': 'Juan Pérez',
            'street': 'Av. Principal 123',
            'phone_number': '1234567890',
            'products': [{'id': 1, 'price': 1600.00, 'quantity': 2}],
            'source': 'landing_page_principal'
        }
        
        response = self.client.post('/order-payment-on-delivery/pod/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['source'], 'landing_page_principal')
    
    def test_create_order_without_source(self):
        """Test crear orden sin campo source (debe usar valor por defecto)"""
        data = {
            'name': 'María García',
            'street': 'Calle Secundaria 456',
            'phone_number': '0987654321',
            'products': [{'id': 1, 'price': 1600.00, 'quantity': 1}]
        }
        
        response = self.client.post('/order-payment-on-delivery/pod/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Debe usar el valor por defecto del modelo
        self.assertEqual(response.data['source'], 'main_landing')
    
    def test_create_order_with_empty_source(self):
        """Test crear orden con source vacío (debe usar valor por defecto)"""
        data = {
            'name': 'Carlos López',
            'street': 'Avenida Central 789',
            'phone_number': '5555555555',
            'products': [{'id': 1, 'price': 1600.00, 'quantity': 1}],
            'source': ''
        }
        
        response = self.client.post('/order-payment-on-delivery/pod/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Debe usar el valor por defecto del modelo cuando source está vacío
        self.assertEqual(response.data['source'], 'main_landing')
    
    def test_create_order_with_long_source(self):
        """Test crear orden con source de 200 caracteres (debe funcionar)"""
        long_source = 'landing_page_' + 'a' * 180  # 200 caracteres exactos
        data = {
            'name': 'Ana Martínez',
            'street': 'Calle Larga 999',
            'phone_number': '1111111111',
            'products': [{'id': 1, 'price': 1600.00, 'quantity': 1}],
            'source': long_source
        }
        
        response = self.client.post('/order-payment-on-delivery/pod/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['source'], long_source)

class SourceFieldModelTestCase(TestCase):
    """Tests para verificar que el campo source se guarda correctamente en el modelo"""
    
    def setUp(self):
        """Configuración inicial"""
        self.state, _ = State.objects.get_or_create(id=1, defaults={'name': "Estado Test"})
        self.user, _ = User.objects.get_or_create(
            username='testuser',
            defaults={
                'email': 'test@test.com',
                'password': 'testpass123'
            }
        )
        self.address, _ = Address.objects.get_or_create(
            street='Calle Test 123',
            defaults={
                'number': 1,
                'interior_number': 1,
                'state': self.state,
                'phone_number': '1234567890'
            }
        )
    
    def test_order_source_field_save(self):
        """Test que el campo source se guarde correctamente en la base de datos"""
        order = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            payment_on_delivery=True,
            source='landing_page_test'
        )
        
        # Verificar que se guardó en la base de datos
        saved_order = Order.objects.get(id=order.id)
        self.assertEqual(saved_order.source, 'landing_page_test')
    
    def test_order_source_field_null(self):
        """Test que el campo source puede ser None (Django no usa default automáticamente)"""
        order = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            payment_on_delivery=True,
            source=None
        )
        
        saved_order = Order.objects.get(id=order.id)
        # Django guarda None cuando se especifica explícitamente
        self.assertIsNone(saved_order.source)
    
    def test_order_source_field_blank(self):
        """Test que el campo source puede estar en blanco (Django no usa default automáticamente)"""
        order = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            payment_on_delivery=True,
            source=''
        )
        
        saved_order = Order.objects.get(id=order.id)
        # Django guarda string vacío cuando se especifica explícitamente
        self.assertEqual(saved_order.source, '')
    
    def test_order_source_field_default_value(self):
        """Test que el campo source usa el valor por defecto cuando no se especifica"""
        order = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            payment_on_delivery=True
            # No especificar source
        )
        
        saved_order = Order.objects.get(id=order.id)
        # Debe usar el valor por defecto del modelo
        self.assertEqual(saved_order.source, 'main_landing')
    
    def test_order_source_field_custom_value(self):
        """Test que el campo source respeta valores personalizados válidos"""
        custom_source = 'custom_landing_page'
        order = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            payment_on_delivery=True,
            source=custom_source
        )
        
        saved_order = Order.objects.get(id=order.id)
        self.assertEqual(saved_order.source, custom_source)
    
    def test_order_source_field_edge_cases(self):
        """Test casos edge del campo source"""
        # Test con espacios en blanco
        order1 = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            payment_on_delivery=True,
            source='   '
        )
        self.assertEqual(order1.source, '   ')  # Django guarda espacios cuando se especifica
        
        # Test con solo espacios
        order2 = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            payment_on_delivery=True,
            source='   '
        )
        self.assertEqual(order2.source, '   ')  # Django guarda espacios cuando se especifica
    
    def test_order_source_field_default_behavior(self):
        """Test que verifica el comportamiento real del valor por defecto"""
        # Test sin especificar source en absoluto
        order = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            payment_on_delivery=True
            # No especificar source
        )
        
        saved_order = Order.objects.get(id=order.id)
        # Solo aquí Django usa el valor por defecto
        self.assertEqual(saved_order.source, 'main_landing')
from django.test import TestCase
from django.urls import reverse
from products.models import Product
from categories.models import Category
from django.core.files.uploadedfile import SimpleUploadedFile
from decimal import Decimal

class ProductCreationTests(TestCase):
    def setUp(self):
        # Crear una categoría para las pruebas
        self.category = Category.objects.create(
            name="Test Category",
            slug="test-category"
        )
        
    def test_create_multiple_products(self):
        """Test que verifica que se pueden crear múltiples productos sin conflicto de IDs"""
        
        # Datos para el primer producto
        product_data_1 = {
            "name": "Producto Test 1",
            "specific_name": "Test Spec 1",
            "price": "100.00",
            "category": self.category.id,
            "weight": "0.5",
            "cost": "0",
            "min_stock": 1,
            "max_stock": 100,
            "es_publico": True
        }
        
        # Datos para el segundo producto
        product_data_2 = {
            "name": "Producto Test 2",
            "specific_name": "Test Spec 2",
            "price": "200.00",
            "category": self.category.id,
            "weight": "1.0",
            "cost": "0",
            "min_stock": 1,
            "max_stock": 100,
            "es_publico": True
        }
        
        # Crear el primer producto
        response1 = self.client.post(
            reverse('product-create'),
            product_data_1,
            format='multipart'
        )
        self.assertEqual(response1.status_code, 201)
        
        # Crear el segundo producto
        response2 = self.client.post(
            reverse('product-create'),
            product_data_2,
            format='multipart'
        )
        self.assertEqual(response2.status_code, 201)
        
        # Verificar que los productos tienen IDs diferentes
        product1_id = response1.json()['id']
        product2_id = response2.json()['id']
        self.assertNotEqual(product1_id, product2_id)
        
        # Verificar que los productos existen en la base de datos
        self.assertTrue(Product.objects.filter(id=product1_id).exists())
        self.assertTrue(Product.objects.filter(id=product2_id).exists()) 
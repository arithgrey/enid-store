from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from products.models import Product
from categories.models import Category
from image.models import Image
import os
from PIL import Image as PILImage
import io

@override_settings(FIXTURE_DIRS=[])  # Evitar cargar fixtures
class ProductIntegrationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Limpiar datos existentes
        Category.objects.all().delete()
        Product.objects.all().delete()
        Image.objects.all().delete()

    def setUp(self):
        # Crear categoría de prueba
        self.category = Category.objects.create(
            name='Test Category',
            slug='test-category'
        )
        
        # Crear imagen de prueba válida usando PIL
        image = PILImage.new('RGB', (100, 100), color='red')
        image_io = io.BytesIO()
        image.save(image_io, format='PNG')
        image_io.seek(0)
        self.test_image = SimpleUploadedFile(
            'test_image.png',
            image_io.getvalue(),
            content_type='image/png'
        )

    def tearDown(self):
        # Limpiar datos
        Category.objects.all().delete()
        Product.objects.all().delete()
        Image.objects.all().delete()

    def test_create_product_with_image(self):
        """
        Test de integración para crear un producto con imagen
        """
        url = '/productos/'
        
        data = {
            'name': 'Test Product',
            'specific_name': 'Test Description',
            'price': '99.99',
            'category': self.category.id,
            'weight': '0.5',
            'cost': '50.00',
            'min_stock': 1,
            'max_stock': 100,
            'es_publico': True,
            'uploaded_images': [self.test_image],
            'main_image_index': 0
        }

        response = self.client.post(url, data, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Image.objects.count(), 1)
        
        product = Product.objects.first()
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.category, self.category)
        self.assertEqual(product.images.count(), 1)
        self.assertTrue(product.images.first().is_main)

    def test_required_fields_validation(self):
        """
        Test de integración para validación de campos requeridos
        """
        url = '/productos/'
        
        data = {
            'name': 'Test Product'
        }

        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Verificar que los errores estén en el formato correcto
        self.assertIn('specific_name', response.data)
        self.assertEqual(response.data['specific_name'], 'Este campo es requerido')
        self.assertIn('price', response.data)
        self.assertEqual(response.data['price'], 'Este campo es requerido')
        self.assertIn('category', response.data)
        self.assertEqual(response.data['category'], 'Este campo es requerido')

    def test_category_validation(self):
        """
        Test de integración para validación de categoría
        """
        url = '/productos/'
        
        data = {
            'name': 'Test Product',
            'specific_name': 'Test Description',
            'price': '99.99',
            'category': 999,  # ID que no existe
            'weight': '0.5',
            'es_publico': True
        }

        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Verificar el formato del error
        self.assertIn('category', response.data)
        self.assertEqual(response.data['category'], 'La categoría especificada no existe')

    def test_product_url_after_creation(self):
        """
        Test de integración para verificar la URL del producto después de crearlo
        """
        url = '/productos/'
        
        data = {
            'name': 'Test Product URL',
            'specific_name': 'Test Description',
            'price': '99.99',
            'category': self.category.id,
            'weight': '0.5',
            'es_publico': True
        }

        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        product = Product.objects.first()
        # La URL debe empezar con /
        self.assertTrue(product.get_absolute_url().startswith('/')) 
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from products.models import Product
from categories.models import Category
from image.models import Image
import os
import tempfile
from PIL import Image as PILImage
from io import BytesIO

class ProductImageIntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Crear una categoría de prueba
        self.category = Category.objects.create(
            name='Test Category'
        )
        
        # Crear imágenes de prueba
        self.test_images = []
        for i in range(3):
            # Crear una imagen temporal usando PIL
            image = PILImage.new('RGB', (100, 100), color='red')
            temp_file = BytesIO()
            image.save(temp_file, 'jpeg')
            temp_file.seek(0)
            
            # Convertir a SimpleUploadedFile
            image_file = SimpleUploadedFile(
                name=f'test_image_{i}.jpg',
                content=temp_file.read(),
                content_type='image/jpeg'
            )
            self.test_images.append(image_file)

    def test_create_product_with_images(self):
        """
        Test de integración para crear un producto con múltiples imágenes
        y verificar que se guarden correctamente.
        """
        # Preparar datos del producto
        product_data = {
            'name': 'Test Product',
            'specific_name': 'Test Description',
            'price': '99.99',
            'category': self.category.id,
            'weight': 0.5,
            'cost': 0,
            'min_stock': 1,
            'max_stock': 100,
            'es_publico': True,
        }

        # Agregar imágenes al request
        for i, image in enumerate(self.test_images):
            product_data[f'uploaded_images[{i}]'] = image
        product_data['main_image_index'] = 0

        # Hacer la petición POST
        response = self.client.post(
            reverse('product-list'),  # Asegúrate de que este es el nombre correcto de tu URL
            product_data,
            format='multipart'
        )

        # Verificar respuesta exitosa
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificar que el producto se creó
        product = Product.objects.get(name='Test Product')
        self.assertIsNotNone(product)
        self.assertEqual(product.category, self.category)
        self.assertEqual(float(product.price), 99.99)

        # Verificar que las imágenes se crearon y asociaron
        product_images = product.images.all()
        self.assertEqual(product_images.count(), 3)
        
        # Verificar que la primera imagen es la principal
        main_images = product_images.filter(is_main=True)
        self.assertEqual(main_images.count(), 1)
        self.assertEqual(main_images.first(), product_images.first())

    def test_create_product_without_images(self):
        """
        Test de integración para verificar que un producto se puede crear
        correctamente sin imágenes.
        """
        product_data = {
            'name': 'Test Product No Images',
            'specific_name': 'Test Description',
            'price': '99.99',
            'category': self.category.id,
            'weight': 0.5,
            'cost': 0,
            'min_stock': 1,
            'max_stock': 100,
            'es_publico': True,
        }

        response = self.client.post(
            reverse('product-list'),
            product_data,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        product = Product.objects.get(name='Test Product No Images')
        self.assertEqual(product.images.count(), 0)

    def test_create_product_invalid_image(self):
        """
        Test de integración para verificar el manejo de imágenes inválidas.
        """
        product_data = {
            'name': 'Test Product Invalid Image',
            'specific_name': 'Test Description',
            'price': '99.99',
            'category': self.category.id,
            'weight': 0.5,
            'cost': 0,
            'min_stock': 1,
            'max_stock': 100,
            'es_publico': True,
        }

        # Crear un archivo que no es una imagen
        invalid_file = SimpleUploadedFile(
            "test.txt",
            b"This is not an image",
            content_type="text/plain"
        )
        product_data['uploaded_images[0]'] = invalid_file

        response = self.client.post(
            reverse('product-list'),
            product_data,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(Product.objects.filter(name='Test Product Invalid Image').exists())

    def test_update_product_images(self):
        """
        Test de integración para verificar la actualización de imágenes
        de un producto existente.
        """
        # Crear producto inicial sin imágenes
        product = Product.objects.create(
            name='Test Product Update',
            specific_name='Test Description',
            price=99.99,
            category=self.category,
            weight=0.5,
            cost=0,
            min_stock=1,
            max_stock=100,
            es_publico=True,
        )

        # Preparar datos para actualización
        update_data = {
            'name': 'Test Product Update',
            'specific_name': 'Updated Description',
            'price': '199.99',
            'category': self.category.id,
        }

        # Agregar una nueva imagen
        update_data['uploaded_images[0]'] = self.test_images[0]
        update_data['main_image_index'] = 0

        response = self.client.patch(
            reverse('product-detail', kwargs={'pk': product.pk}),
            update_data,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verificar que la imagen se agregó
        product.refresh_from_db()
        self.assertEqual(product.images.count(), 1)
        self.assertTrue(product.images.first().is_main)
        self.assertEqual(float(product.price), 199.99)

    def tearDown(self):
        # Limpiar archivos temporales
        for image in Image.objects.all():
            if image.image and os.path.isfile(image.image.path):
                os.remove(image.image.path) 
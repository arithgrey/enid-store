from django.test import TestCase
from rest_framework.test import APITestCase
from products.models import Product
from products.serializers import ProductSerializer
from categories.models import Category

class ProductSerializerTest(APITestCase):
    def setUp(self):
        # Crear una categoría de prueba
        self.category = Category.objects.create(
            name='Test Category'
        )
        
        # Crear un producto de prueba
        self.product = Product.objects.create(
            id=2001,  # ID alto para evitar conflictos
            name='Test Product',
            specific_name='Test Description',
            price=99.99,
            category=self.category,
            weight=0.5,
            cost=0,
            min_stock=1,
            max_stock=100,
            es_publico=True,
        )

    def test_serializer_fields_completeness(self):
        """Test que verifica que todos los campos del modelo están en la serialización"""
        serializer = ProductSerializer(instance=self.product)
        data = serializer.data
        
        expected_fields = {
            'id', 'name', 'specific_name', 'price', 'category',
            'weight', 'cost', 'count_discs', 'top_seller', 'primary',
            'slug', 'es_publico', 'min_stock', 'max_stock',
            'express_payment_link', 'images', 'short_name',
            'formatted_price', 'formatted_cost', 'formatted_weight'
        }
        
        self.assertEqual(set(data.keys()), expected_fields)

    def test_serializer_method_fields(self):
        """Test que verifica que los campos de método funcionan correctamente"""
        serializer = ProductSerializer(instance=self.product)
        data = serializer.data
        
        self.assertEqual(data['short_name'], self.product.name[:82])
        self.assertEqual(data['formatted_price'], f'${self.product.price:.2f}')
        self.assertEqual(data['formatted_weight'], f"{self.product.weight} Kg")

    def test_serializer_create_product(self):
        """Test que verifica la creación de un producto a través del serializer"""
        data = {
            'name': 'New Product',
            'specific_name': 'New Description',
            'price': '199.99',
            'category': self.category.id,
            'weight': 1.5,
            'cost': 50,
            'min_stock': 5,
            'max_stock': 200,
            'es_publico': True
        }
        
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        product = serializer.save()
        
        self.assertEqual(product.name, data['name'])
        self.assertEqual(float(product.price), float(data['price']))
        self.assertEqual(product.category, self.category)

    def test_serializer_update_product(self):
        """Test que verifica la actualización de un producto a través del serializer"""
        data = {
            'name': 'Updated Product',
            'specific_name': 'Updated Description',
            'price': '299.99'
        }
        
        serializer = ProductSerializer(instance=self.product, data=data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_product = serializer.save()
        
        self.assertEqual(updated_product.name, data['name'])
        self.assertEqual(float(updated_product.price), float(data['price']))

    def test_serializer_validation(self):
        """Test que verifica la validación del serializer"""
        data = {
            'name': 'Invalid Product',
            'specific_name': 'Invalid Description',
            'price': 'not a price',  # Precio inválido
            'category': 999  # Categoría que no existe
        }
        
        serializer = ProductSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('price', serializer.errors)
        self.assertIn('category', serializer.errors)

    def test_serializer_es_publico_default_in_create(self):
        """Test que verifica que es_publico tiene valor por defecto al crear"""
        data = {
            'name': 'Public Product',
            'specific_name': 'Public Description',
            'price': '99.99',
            'category': self.category.id
        }
        
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        product = serializer.save()
        
        self.assertTrue(product.es_publico)  # Valor por defecto es True

    def test_serializer_with_es_publico_false(self):
        """Test que verifica la serialización cuando es_publico es False"""
        self.product.es_publico = False
        self.product.save()
        
        serializer = ProductSerializer(instance=self.product)
        data = serializer.data
        
        self.assertFalse(data['es_publico']) 
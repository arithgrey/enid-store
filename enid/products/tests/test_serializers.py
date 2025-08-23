from django.test import TestCase
from products.models import Product
from products.serializers import ProductSerializer, ProductItemSerializer
from categories.models import Category
from product_group.models import ProductGroup


class ProductSerializerTest(TestCase):
    """Tests para los serializers de Product incluyendo el nuevo campo es_publico"""

    def setUp(self):
        """Configuración inicial para los tests"""
        # Crear categoría de prueba (AutoSlugField se genera automáticamente)
        self.category = Category.objects.create(
            name="Test Category"
        )
        
        # Crear grupo de productos de prueba (solo tiene name y category)
        self.product_group = ProductGroup.objects.create(
            name="Test Group"
        )
        
        # Crear producto de prueba
        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            price=99.99,
            cost=50.00,
            weight=1.5,
            specific_name="Test Specific Name",
            product_group=self.product_group,
            name_product_group="Test Group Name",
            es_publico=True
        )

    def test_product_serializer_includes_es_publico(self):
        """Test que verifica que ProductSerializer incluye el campo es_publico"""
        serializer = ProductSerializer(self.product)
        data = serializer.data
        
        # Verificar que es_publico está presente
        self.assertIn('es_publico', data)
        self.assertTrue(data['es_publico'])
        
        # Verificar que otros campos importantes están presentes
        self.assertIn('name', data)
        self.assertIn('price', data)
        self.assertIn('category', data)

    def test_product_item_serializer_includes_es_publico(self):
        """Test que verifica que ProductItemSerializer incluye el campo es_publico"""
        serializer = ProductItemSerializer(self.product)
        data = serializer.data
        
        # Verificar que es_publico está presente
        self.assertIn('es_publico', data)
        self.assertTrue(data['es_publico'])

    def test_serializer_with_es_publico_false(self):
        """Test que verifica la serialización cuando es_publico es False"""
        # Cambiar es_publico a False
        self.product.es_publico = False
        self.product.save()
        
        serializer = ProductSerializer(self.product)
        data = serializer.data
        
        # Verificar que es_publico es False
        self.assertFalse(data['es_publico'])

    def test_serializer_fields_completeness(self):
        """Test que verifica que todos los campos del modelo están en la serialización"""
        serializer = ProductSerializer(self.product)
        data = serializer.data
        
        # Campos básicos que deben estar presentes
        expected_fields = [
            'id', 'name', 'price', 'cost', 'weight', 'count_discs',
            'top_seller', 'primary', 'slug', 'specific_name',
            'product_group', 'name_product_group', 'express_payment_link',
            'min_stock', 'max_stock', 'es_publico', 'category'
        ]
        
        for field in expected_fields:
            self.assertIn(field, data, f"El campo {field} no está presente en la serialización")

    def test_serializer_method_fields(self):
        """Test que verifica que los campos de método funcionan correctamente"""
        serializer = ProductSerializer(self.product)
        data = serializer.data
        
        # Verificar campos de método
        self.assertIn('short_name', data)
        self.assertIn('formatted_price', data)
        self.assertIn('formatted_cost', data)
        self.assertIn('formatted_weight', data)
        
        # Verificar que short_name está truncado correctamente
        self.assertEqual(len(data['short_name']), 82)

    def test_serializer_validation(self):
        """Test que verifica la validación del serializer"""
        # Crear datos válidos
        valid_data = {
            'category': self.category.id,
            'name': 'Valid Product',
            'price': 199.99,
            'cost': 100.00,
            'weight': 2.0,
            'specific_name': 'Valid Specific Name',
            'es_publico': True
        }
        
        serializer = ProductSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid(), f"Errores de validación: {serializer.errors}")

    def test_serializer_create_product(self):
        """Test que verifica la creación de un producto a través del serializer"""
        product_data = {
            'category': self.category.id,
            'name': 'Created Product',
            'price': 299.99,
            'cost': 150.00,
            'weight': 3.0,
            'specific_name': 'Created Specific Name',
            'es_publico': False
        }
        
        serializer = ProductSerializer(data=product_data)
        self.assertTrue(serializer.is_valid())
        
        product = serializer.save()
        
        # Verificar que el producto se creó correctamente
        self.assertEqual(product.name, 'Created Product')
        self.assertFalse(product.es_publico)
        self.assertEqual(product.price, 299.99)

    def test_serializer_update_product(self):
        """Test que verifica la actualización de un producto a través del serializer"""
        update_data = {
            'name': 'Updated Product Name',
            'es_publico': False,
            'price': 149.99
        }
        
        serializer = ProductSerializer(self.product, data=update_data, partial=True)
        self.assertTrue(serializer.is_valid())
        
        updated_product = serializer.save()
        
        # Verificar que los campos se actualizaron
        self.assertEqual(updated_product.name, 'Updated Product Name')
        self.assertFalse(updated_product.es_publico)
        self.assertEqual(updated_product.price, 149.99)
        
        # Verificar que otros campos no cambiaron
        self.assertEqual(updated_product.cost, 50.00)
        self.assertEqual(updated_product.weight, 1.5)

    def test_serializer_es_publico_default_in_create(self):
        """Test que verifica que es_publico tiene valor por defecto al crear"""
        product_data = {
            'category': self.category.id,
            'name': 'Default Public Product',
            'price': 99.99,
            'cost': 50.00,
            'weight': 1.0,
            'specific_name': 'Default Specific Name'
            # No especificamos es_publico
        }
        
        serializer = ProductSerializer(data=product_data)
        self.assertTrue(serializer.is_valid())
        
        product = serializer.save()
        
        # Verificar que es_publico tiene el valor por defecto True
        self.assertTrue(product.es_publico) 
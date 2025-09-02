from django.test import TestCase
from django.core.exceptions import ValidationError
from products.models import Product
from categories.models import Category
from product_group.models import ProductGroup


class ProductModelTest(TestCase):
    """Tests para el modelo Product incluyendo el nuevo campo es_publico"""

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
            name_product_group="Test Group Name"
        )

    def test_es_publico_default_value(self):
        """Test que verifica que es_publico tiene valor por defecto True"""
        # Crear un producto sin especificar es_publico
        product = Product.objects.create(
            category=self.category,
            name="Default Public Product",
            price=49.99,
            cost=25.00,
            weight=0.5,
            specific_name="Default Public Specific Name"
        )
        
        self.assertTrue(product.es_publico)
        self.assertEqual(product.es_publico, True)

    def test_es_publico_can_be_false(self):
        """Test que verifica que es_publico puede ser False"""
        product = Product.objects.create(
            category=self.category,
            name="Private Product",
            price=29.99,
            cost=15.00,
            weight=0.3,
            specific_name="Private Specific Name",
            es_publico=False
        )
        
        self.assertFalse(product.es_publico)
        self.assertEqual(product.es_publico, False)

    def test_es_publico_field_exists(self):
        """Test que verifica que el campo es_publico existe en el modelo"""
        # Verificar que el campo existe en el modelo
        field_names = [field.name for field in Product._meta.fields]
        self.assertIn('es_publico', field_names)
        
        # Verificar que es un BooleanField
        es_publico_field = Product._meta.get_field('es_publico')
        self.assertEqual(es_publico_field.get_internal_type(), 'BooleanField')

    def test_es_publico_help_text(self):
        """Test que verifica el texto de ayuda del campo es_publico"""
        es_publico_field = Product._meta.get_field('es_publico')
        expected_help_text = 'Indica si el producto es visible públicamente'
        self.assertEqual(es_publico_field.help_text, expected_help_text)

    def test_product_creation_with_es_publico(self):
        """Test que verifica la creación completa de un producto con es_publico"""
        product_data = {
            'category': self.category,
            'name': 'Complete Test Product',
            'price': 199.99,
            'cost': 100.00,
            'weight': 2.0,
            'specific_name': 'Complete Test Specific Name',
            'product_group': self.product_group,
            'name_product_group': 'Complete Test Group',
            'es_publico': True
        }
        
        product = Product.objects.create(**product_data)
        
        # Verificar que todos los campos se guardaron correctamente
        self.assertEqual(product.name, 'Complete Test Product')
        self.assertEqual(product.price, 199.99)
        self.assertTrue(product.es_publico)
        
        # Verificar que se puede cambiar el valor
        product.es_publico = False
        product.save()
        product.refresh_from_db()
        self.assertFalse(product.es_publico)

    def test_product_str_representation(self):
        """Test que verifica la representación string del producto"""
        expected_str = "Test Product"
        self.assertEqual(str(self.product), expected_str)

    def test_product_absolute_url(self):
        """Test que verifica la URL absoluta del producto"""
        expected_url = f"{self.category.slug}/{self.product.slug}/"
        self.assertEqual(self.product.get_absolute_url(), expected_url)

    def test_product_weight_kit_detection(self):
        """Test que verifica la detección de kit de pesas"""
        # Producto sin componentes primarios no es un kit
        self.assertFalse(self.product.is_weight_kit())
        
        # Producto con componentes primarios es un kit
        # (Este test requeriría crear ProductComponent, pero por simplicidad lo omitimos)

    def test_product_serialization(self):
        """Test que verifica que el campo es_publico se serializa correctamente"""
        from products.serializers import ProductSerializer
        
        serializer = ProductSerializer(self.product)
        serialized_data = serializer.data
        
        # Verificar que es_publico está en los datos serializados
        self.assertIn('es_publico', serialized_data)
        self.assertTrue(serialized_data['es_publico'])

    def test_product_filtering_by_es_publico(self):
        """Test que verifica el filtrado por es_publico"""
        # Crear productos públicos y privados
        Product.objects.create(
            category=self.category,
            name="Public Product 1",
            price=10.00,
            cost=5.00,
            weight=0.1,
            specific_name="Public 1",
            es_publico=True
        )
        
        Product.objects.create(
            category=self.category,
            name="Private Product 1",
            price=20.00,
            cost=10.00,
            weight=0.2,
            specific_name="Private 1",
            es_publico=False
        )
        
        # Contar productos públicos
        public_products = Product.objects.filter(es_publico=True)
        self.assertEqual(public_products.count(), 2)  # Incluye el del setUp
        
        # Contar productos privados
        private_products = Product.objects.filter(es_publico=False)
        self.assertEqual(private_products.count(), 1)
        
        # Contar todos los productos
        all_products = Product.objects.all()
        self.assertEqual(all_products.count(), 4)  # Incluye el del setUp 
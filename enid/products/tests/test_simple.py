from django.test import TestCase
from products.models import Product


class SimpleProductTest(TestCase):
    """Test simple para verificar que el campo es_publico funciona"""

    def test_es_publico_field_exists(self):
        """Test que verifica que el campo es_publico existe en el modelo"""
        # Verificar que el campo existe en el modelo
        field_names = [field.name for field in Product._meta.fields]
        self.assertIn('es_publico', field_names)
        
        # Verificar que es un BooleanField
        es_publico_field = Product._meta.get_field('es_publico')
        self.assertEqual(es_publico_field.get_internal_type(), 'BooleanField')

    def test_es_publico_default_value(self):
        """Test que verifica que es_publico tiene valor por defecto True"""
        # Verificar el valor por defecto del campo
        es_publico_field = Product._meta.get_field('es_publico')
        self.assertEqual(es_publico_field.default, True)

    def test_es_publico_help_text(self):
        """Test que verifica el texto de ayuda del campo es_publico"""
        es_publico_field = Product._meta.get_field('es_publico')
        expected_help_text = 'Indica si el producto es visible públicamente'
        self.assertEqual(es_publico_field.help_text, expected_help_text)

    def test_es_publico_field_type(self):
        """Test que verifica el tipo de campo es_publico"""
        es_publico_field = Product._meta.get_field('es_publico')
        
        # Verificar que es un BooleanField
        self.assertEqual(es_publico_field.get_internal_type(), 'BooleanField')
        
        # Verificar que no es null
        self.assertFalse(es_publico_field.null)
        
        # Verificar que no es blank
        self.assertFalse(es_publico_field.blank) 
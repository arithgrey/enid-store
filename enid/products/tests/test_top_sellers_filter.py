from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Product
from categories.models import Category
from product_group.models import ProductGroup


class TopSellersFilterTest(APITestCase):
    """Tests para verificar que el endpoint top-sellers solo muestra productos públicos"""

    def setUp(self):
        """Configuración inicial para los tests"""
        # Crear categoría de prueba
        self.category = Category.objects.create(
            name="Test Category"
        )
        
        # Crear grupo de productos de prueba
        self.product_group = ProductGroup.objects.create(
            name="Test Group"
        )
        
        # Crear productos de prueba
        self.public_top_seller = Product.objects.create(
            category=self.category,
            name="Public Top Seller",
            price=99.99,
            cost=50.00,
            weight=1.5,
            specific_name="Public Top Seller Specific Name",
            product_group=self.product_group,
            name_product_group="Public Top Seller Group",
            top_seller=True,
            es_publico=True
        )
        
        self.private_top_seller = Product.objects.create(
            category=self.category,
            name="Private Top Seller",
            price=149.99,
            cost=75.00,
            weight=2.0,
            specific_name="Private Top Seller Specific Name",
            product_group=self.product_group,
            name_product_group="Private Top Seller Group",
            top_seller=True,
            es_publico=False
        )
        
        self.regular_product = Product.objects.create(
            category=self.category,
            name="Regular Product",
            price=79.99,
            cost=40.00,
            weight=1.0,
            specific_name="Regular Product Specific Name",
            product_group=self.product_group,
            name_product_group="Regular Product Group",
            top_seller=False,
            es_publico=True
        )

    def test_top_sellers_only_shows_public_products(self):
        """Test que verifica que top-sellers solo muestra productos públicos"""
        url = reverse('product-top-sellers')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        # Verificar que solo se devuelven productos top_seller que sean públicos
        products = response.data['results'] if 'results' in response.data else response.data
        
        # Verificar que el producto público top_seller está presente
        public_product_ids = [p['id'] for p in products]
        self.assertIn(self.public_top_seller.id, public_product_ids)
        
        # Verificar que el producto privado top_seller NO está presente
        self.assertNotIn(self.private_top_seller.id, public_product_ids)
        
        # Verificar que todos los productos devueltos tienen es_publico=True
        for product in products:
            self.assertTrue(product['es_publico'], 
                          f"Producto {product['id']} debe ser público")

    def test_private_top_seller_not_in_response(self):
        """Test que verifica que productos top_seller privados no aparecen"""
        url = reverse('product-top-sellers')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        products = response.data['results'] if 'results' in response.data else response.data
        
        # Verificar que el producto privado top_seller NO está en la respuesta
        private_product_ids = [p['id'] for p in products]
        self.assertNotIn(self.private_top_seller.id, private_product_ids)

    def test_public_top_seller_in_response(self):
        """Test que verifica que productos top_seller públicos aparecen"""
        url = reverse('product-top-sellers')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        products = response.data['results'] if 'results' in response.data else response.data
        
        # Verificar que el producto público top_seller está en la respuesta
        public_product_ids = [p['id'] for p in products]
        self.assertIn(self.public_top_seller.id, public_product_ids)

    def test_regular_product_not_in_top_sellers(self):
        """Test que verifica que productos regulares no aparecen en top-sellers"""
        url = reverse('product-top-sellers')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        products = response.data['results'] if 'results' in response.data else response.data
        
        # Verificar que el producto regular NO está en top-sellers
        regular_product_ids = [p['id'] for p in products]
        self.assertNotIn(self.regular_product.id, regular_product_ids)

    def test_top_sellers_count_correct(self):
        """Test que verifica que el conteo de productos es correcto"""
        url = reverse('product-top-sellers')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        # Debería haber solo 1 producto top_seller público
        expected_count = 1
        
        if 'count' in response.data:
            # Si hay paginación
            self.assertEqual(response.data['count'], expected_count)
        else:
            # Si no hay paginación
            self.assertEqual(len(response.data), expected_count)

    def test_top_sellers_response_structure(self):
        """Test que verifica la estructura de la respuesta"""
        url = reverse('product-top-sellers')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        products = response.data['results'] if 'results' in response.data else response.data
        
        # Verificar que cada producto tiene los campos necesarios
        required_fields = ['id', 'name', 'price', 'top_seller', 'es_publico']
        
        for product in products:
            for field in required_fields:
                self.assertIn(field, product, 
                            f"El campo {field} debe estar presente en el producto {product['id']}")
            
            # Verificar que top_seller es True
            self.assertTrue(product['top_seller'], 
                          f"Producto {product['id']} debe ser top_seller")
            
            # Verificar que es_publico es True
            self.assertTrue(product['es_publico'], 
                          f"Producto {product['id']} debe ser público") 
from django.test import TestCase
from rest_framework.test import APITestCase
from products.models import Product
from categories.models import Category

class TopSellersFilterTest(APITestCase):
    def setUp(self):
        # Crear categoría de prueba
        self.category = Category.objects.create(
            name='Test Category'
        )
        
        # Crear productos de prueba
        self.public_top_seller = Product.objects.create(
            id=3001,  # ID alto para evitar conflictos
            name='Public Top Seller',
            specific_name='Public Top Seller Description',
            price=99.99,
            category=self.category,
            top_seller=True,
            es_publico=True
        )
        
        self.private_top_seller = Product.objects.create(
            id=3002,  # ID alto para evitar conflictos
            name='Private Top Seller',
            specific_name='Private Top Seller Description',
            price=99.99,
            category=self.category,
            top_seller=True,
            es_publico=False
        )
        
        self.regular_product = Product.objects.create(
            id=3003,  # ID alto para evitar conflictos
            name='Regular Product',
            specific_name='Regular Product Description',
            price=99.99,
            category=self.category,
            top_seller=False,
            es_publico=True
        )

    def test_public_top_seller_in_response(self):
        """Test que verifica que productos top_seller públicos aparecen"""
        response = self.client.get('/enid/productos/top-sellers/')
        self.assertEqual(response.status_code, 200)
        
        products = response.data
        public_product_ids = [p['id'] for p in products]
        self.assertIn(self.public_top_seller.id, public_product_ids)

    def test_private_top_seller_not_in_response(self):
        """Test que verifica que productos top_seller privados no aparecen"""
        response = self.client.get('/enid/productos/top-sellers/')
        self.assertEqual(response.status_code, 200)
        
        products = response.data
        private_product_ids = [p['id'] for p in products]
        self.assertNotIn(self.private_top_seller.id, private_product_ids)

    def test_regular_product_not_in_top_sellers(self):
        """Test que verifica que productos regulares no aparecen en top-sellers"""
        response = self.client.get('/enid/productos/top-sellers/')
        self.assertEqual(response.status_code, 200)
        
        products = response.data
        regular_product_ids = [p['id'] for p in products]
        self.assertNotIn(self.regular_product.id, regular_product_ids)

    def test_top_sellers_count_correct(self):
        """Test que verifica que el conteo de productos es correcto"""
        response = self.client.get('/enid/productos/top-sellers/')
        self.assertEqual(response.status_code, 200)
        
        products = response.data
        self.assertEqual(len(products), 1)  # Solo debe aparecer el top seller público

    def test_top_sellers_only_shows_public_products(self):
        """Test que verifica que top-sellers solo muestra productos públicos"""
        response = self.client.get('/enid/productos/top-sellers/')
        self.assertEqual(response.status_code, 200)
        
        products = response.data
        for product in products:
            self.assertTrue(product['es_publico'])

    def test_top_sellers_response_structure(self):
        """Test que verifica la estructura de la respuesta"""
        response = self.client.get('/enid/productos/top-sellers/')
        self.assertEqual(response.status_code, 200)
        
        products = response.data
        for product in products:
            self.assertIn('id', product)
            self.assertIn('name', product)
            self.assertIn('price', product)
            self.assertIn('es_publico', product)
            self.assertIn('top_seller', product)
            self.assertTrue(product['top_seller']) 
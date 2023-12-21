from django.test import TestCase
from rest_framework.test import APIClient
from products.models import Product
from django.contrib.auth.models import User
from cart.services.without_authentication import WithoutAuthentication
from cart.models import Cart
from item_cart.models import ItemCart

class CartVuewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name='Test Product1', price=10.0)
        self.user = User.objects.create(username='testuser', password='testpassword')        
        self.user_cart = Cart.objects.create(user=self.user)

        self.without_authentication_service = WithoutAuthentication()
        self.without_session_cart = self.without_authentication_service.get_or_create_cart(session={})
        self.item_cart = ItemCart.objects.create(cart=self.user_cart, product=self.product, quantity=3)        

    
    def test_products(self):
        self.client.force_authenticate(user=self.user)
        data = {'product_id': self.product.id, 'quantity': 1}
        response = self.client.post('/api/item-cart/add_to_cart/', data, format='json')                
        response = self.client.get('/api/cart/productos/')  
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertGreater(len(response.data), 0)


    def test_products_without_authentication(self):
    
        data = {'product_id': self.product.id, 'quantity': 1}
        response = self.client.post('/api/item-cart/add_to_cart/', data, format='json')                
        response = self.client.get('/api/cart/productos/')  

        list_products_item_cart = response.data
        item_cart = list_products_item_cart[0]
        

        self.assertEqual(item_cart['product_name'], self.product.name)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)        
        self.assertGreaterEqual(len(response.data), 0)


# Create your tests here.
class WithoutAuthenticationTestCase(TestCase):
        
    def test_create_cart_without_authenticated_user(self):

        print("[TEST][CartService] - Se crea o consigue un Cart correcto sin ser un usuario autenticado---")        
        without_authentication = WithoutAuthentication()
        user_cart = without_authentication.get_or_create_cart(session={})
        self.assertIsInstance(user_cart, Cart)


    
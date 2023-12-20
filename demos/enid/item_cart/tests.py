from django.test import TestCase
from item_cart.services.session_cart_service import CartService
from cart.services.without_authentication import WithoutAuthentication
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from item_cart.models import ItemCart
from products.models import Product
from cart.models import Cart
import random

class ItemCartViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name='Test Product', price=10.0)
        self.user = User.objects.create(username='testuser', password='testpassword')


    def test_add_to_cart_authenticated_user(self):
        print("[TEST] - Agregar productos al carro autenticados")
        
        self.client.force_authenticate(user=self.user)                
        for _ in range(5):
            quantity = random.randint(1,9)
            data = {'product_id' : self.product.id, 'quantity':quantity}
            response = self.client.post('/api/item-cart/add_to_cart/', data, format='json')
            
            self.assertEqual(response.status_code, 201)
            

    def test_add_to_cart_whithout_authentication(self):
        print("[TEST] - Agregar productos al carro sin estar autenticados")

        ItemCart.objects.all().delete()        
        for _ in range(4):                        
            
            quantity = random.randint(1,9)
            data = {'product_id': self.product.id, 'quantity': quantity}
            response = self.client.post('/api/item-cart/add_to_cart/', data, format='json')        
            self.assertEqual(response.status_code, 201)                        

        

class CartServiceTestCase(TestCase):
    def setUp(self):
        # Crear productos y usuario para usar en las pruebas
        self.product = Product.objects.create(name='Producto de Prueba', price=10.0)
        self.user = User.objects.create(username='testuser', password='testpassword')

    def test_add_to_cart_without_authentication(self):
        print("[TEST][CartService] - Agregar productos al carro sin autenticación")
        service = CartService()
        session = {}        
        item = service.add_to_cart(
            user=None, product=self.product, quantity=5, session=session)        
        self.assertEqual(item.quantity, 5)
        self.assertEqual(item.product, self.product)

    def test_add_to_cart(self):
        print("[TEST][CartService] - Agregar productos al carro usuario autenticado")
        service = CartService()
        session = {}        
        item = service.add_to_cart(
            user=self.user, product=self.product, quantity=5, session=session)
        self.assertEqual(item.quantity, 5)
        self.assertEqual(item.product, self.product)
    
    def test_create_cart_without_authenticated_user(self):
        print("[TEST][CartService] - Se crea un Cart correcto sin ser un usuario autenticado1")        
        without_authentication = WithoutAuthentication()
        user_cart = without_authentication.get_or_create_cart(session={})
        self.assertIsInstance(user_cart, Cart)
    
    def test_add_quantity_to_existing_product(self):
        print("[TEST][CartService] - Suma cantidades a los item cart, usuario registrado")        
        service = CartService()
        session = {}        
        a = 0
        for _ in range(5):

            quantity = random.randint(1,10)
            item = service.add_to_cart(user=self.user, product=self.product, quantity=quantity, session=session)
            a =  a + quantity 

        self.assertEqual(item.quantity, a)

        
    def test_add_quantity_to_existing_product(self):
        print("[TEST][CartService] - Suma cantidades a los item cart, usuario sin registro.-")        
        service = CartService()
        session = {}        
        a = 0
        for _ in range(5):
            
            quantity = random.randint(1,10)
            item = service.add_to_cart(user=None, product=self.product, quantity=quantity, session=session)
            a =  a + quantity 

        self.assertEqual(item.quantity, a)

        
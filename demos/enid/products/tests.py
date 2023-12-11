from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from cart.models import Cart
from products.product_cart import  DefaultProductCart
from products.services import ServiceProductCart
from unittest.mock import Mock
from item_cart.models import ItemCart

class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=10.0)
        self.cart = Cart.objects.create(user=self.user)        

    def test_add_product_to_cart_by_default(self):
        
        # Usamos los objetos creados en setUp
        product_cart_by_default = DefaultProductCart()
        service_product_cart = ServiceProductCart(product_cart_by_default) 

        # Utilizamos la tarjeta creada en setUp
        service_product_cart.add_product(cart=self.cart, product=self.product, amount=12)

        # Verificamos que la tarjeta tenga el producto agregado
        #self.assertEqual(self.cart.itemcart_set.count(), 1)
        
        # Obtener el objeto ItemCart creado
        #new_item_cart = self.cart.itemcart_set.first()
        
        # Verificar que el objeto creado sea una instancia de ItemCart
        #self.assertIsInstance(new_item_cart, ItemCart)
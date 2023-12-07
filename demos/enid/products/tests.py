from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Card, ItemCard
from .product_card import  DefaultProductCard
from .services import ServiceProductCard


class CardModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=10.0)
        self.card = Card.objects.create(user=self.user)

    def test_add_product_to_card_by_default(self):
        
        # Usamos los objetos creados en setUp
        product_card_by_default = DefaultProductCard()
        service_product_card = ServiceProductCard(product_card_by_default) 

        # Utilizamos la tarjeta creada en setUp
        service_product_card.add_product(card=self.card, product=self.product, amount=12)

        # Verificamos que la tarjeta tenga el producto agregado
        self.assertEqual(self.card.itemcard_set.count(), 1)
        
        # Obtener el objeto ItemCard creado
        new_item_card = self.card.itemcard_set.first()
        
        # Verificar que el objeto creado sea una instancia de ItemCard
        self.assertIsInstance(new_item_card, ItemCard)
        
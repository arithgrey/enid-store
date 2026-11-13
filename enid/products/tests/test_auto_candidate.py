from django.test import TestCase
from products.models import Product
from order.models import Order
from item_order.models import ItemOrder


def _product_in_state(certification='published'):
    # Reusamos un producto sembrado (post_migrate) para evitar colisiones con la
    # secuencia de Postgres, mismo patrón que revenue/tests/test_monthly.py.
    product = Product.objects.first()
    product.certification = certification
    product.save(update_fields=['certification'])
    return product


class AutoCandidateTest(TestCase):
    def test_income_order_promotes_published_to_candidate(self):
        product = _product_in_state('published')
        order = Order.objects.create(status='delivered')
        ItemOrder.objects.create(order=order, product=product, quantity=1, price=100)
        product.refresh_from_db()
        self.assertEqual(product.certification, 'candidate')

    def test_non_income_status_keeps_published(self):
        product = _product_in_state('published')
        order = Order.objects.create(status='pending')
        ItemOrder.objects.create(order=order, product=product, quantity=1, price=100)
        product.refresh_from_db()
        self.assertEqual(product.certification, 'published')

    def test_income_order_never_degrades_certified(self):
        product = _product_in_state('certified')
        order = Order.objects.create(status='delivered')
        ItemOrder.objects.create(order=order, product=product, quantity=1, price=100)
        product.refresh_from_db()
        self.assertEqual(product.certification, 'certified')

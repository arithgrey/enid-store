from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from order.models import Order
from item_order.models import ItemOrder
from products.models import Product
from categories.models import Category
from revenue.tests.test_monthly import _make_address, _make_user
from datetime import datetime
import pytz


def _get_or_create_two_products():
    """
    Returns (prod_a, prod_b) avoiding sequence conflicts with seeded data.
    Uses existing products when available, creates only what's missing.
    """
    existing = list(Product.objects.all()[:2])
    if len(existing) >= 2:
        return existing[0], existing[1]
    cat, _ = Category.objects.get_or_create(name='Cat')
    if len(existing) == 1:
        prod_b = Product.objects.create(
            name='Carpa 3x3 Test', specific_name='Carpa 3x3 Test',
            price=100, category=cat,
        )
        return existing[0], prod_b
    prod_a = Product.objects.create(
        name='Kit Pesas Test', specific_name='Kit Pesas Test',
        price=100, category=cat,
    )
    prod_b = Product.objects.create(
        name='Carpa 3x3 Test', specific_name='Carpa 3x3 Test',
        price=100, category=cat,
    )
    return prod_a, prod_b


def _make_order_with_products(address, user, status_val, year, month, items):
    """
    items = [(product, price, qty), ...]
    """
    dt = datetime(year, month, 15, 12, 0, 0, tzinfo=pytz.UTC)
    order = Order.objects.create(shipping_address=address, user=user, status=status_val)
    Order.objects.filter(pk=order.pk).update(created_at=dt)
    for product, price, qty in items:
        ItemOrder.objects.create(order=order, product=product, quantity=qty, price=price)
    return order


class ByProductRevenueTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser('admin@t.com', 'admin@t.com', 'pass')
        self.client.force_authenticate(user=self.admin)
        self.address = _make_address()
        self.user = _make_user()
        self.prod_a, self.prod_b = _get_or_create_two_products()

    def test_ordered_by_amount_desc(self):
        _make_order_with_products(
            self.address, self.user, 'payment_confirmed', 2025, 6,
            [(self.prod_a, 100, 3), (self.prod_b, 100, 1)]
        )
        resp = self.client.get('/revenue/by-product/', {'year': 2025, 'month': 6})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        amounts = [d['amount'] for d in resp.data]
        self.assertEqual(amounts, sorted(amounts, reverse=True))

    def test_pct_sums_to_100(self):
        _make_order_with_products(
            self.address, self.user, 'payment_confirmed', 2025, 6,
            [(self.prod_a, 100, 3), (self.prod_b, 100, 1)]
        )
        resp = self.client.get('/revenue/by-product/', {'year': 2025, 'month': 6})
        total_pct = sum(d['pct'] for d in resp.data)
        self.assertAlmostEqual(total_pct, 100.0, places=0)

    def test_amount_calculation(self):
        _make_order_with_products(
            self.address, self.user, 'delivered', 2025, 7,
            [(self.prod_a, 500, 2)]
        )
        resp = self.client.get('/revenue/by-product/', {'year': 2025, 'month': 7})
        self.assertEqual(float(resp.data[0]['amount']), 1000.0)

    def test_image_field_present(self):
        _make_order_with_products(
            self.address, self.user, 'payment_confirmed', 2025, 8,
            [(self.prod_a, 100, 1)]
        )
        resp = self.client.get('/revenue/by-product/', {'year': 2025, 'month': 8})
        self.assertIn('image', resp.data[0])

    def test_empty_month_returns_empty_list(self):
        resp = self.client.get('/revenue/by-product/', {'year': 2099, 'month': 1})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(list(resp.data), [])

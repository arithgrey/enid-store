from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from order.models import Order
from item_order.models import ItemOrder
from address.models import Address
from state.models import State
from products.models import Product
from categories.models import Category
from datetime import datetime
import pytz


RECIBIDOS = ['payment_confirmed', 'delivered', 'cash_on_delivery']
PENDIENTES = ['pending', 'preparing', 'ready_for_shipping', 'in_transit', 'ready_for_pickup']
EXCLUIDOS  = ['returned', 'refund_processed', 'canceled']


def _make_address():
    state, _ = State.objects.get_or_create(name="CDMX")
    return Address.objects.create(
        postal_code='12345', street='Calle', number=1,
        interior_number=1, colony='Col', delegation_or_municipality='Del',
        city='CDMX', state=state, phone_number='5551234567'
    )


def _make_user(username='test@test.com'):
    return User.objects.create_user(username=username, password='pass', email=username)


def _make_product():
    # Reuse an existing product to avoid sequence conflicts with seeded data.
    # ItemOrder stores its own price/quantity so the product's price is irrelevant.
    product = Product.objects.first()
    if product is not None:
        return product
    cat, _ = Category.objects.get_or_create(name='Cat')
    return Product.objects.create(
        name='Prod',
        specific_name='Prod Specific',
        price=100,
        category=cat,
    )


def _make_order(address, user, status_val, year, month, price=100, qty=1):
    dt = datetime(year, month, 15, 12, 0, 0, tzinfo=pytz.UTC)
    order = Order.objects.create(
        shipping_address=address, user=user, status=status_val
    )
    Order.objects.filter(pk=order.pk).update(created_at=dt)
    order.refresh_from_db()
    product = _make_product()
    ItemOrder.objects.create(order=order, product=product, quantity=qty, price=price)
    return order


class MonthlyRevenueTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser('admin@t.com', 'admin@t.com', 'pass')
        self.client.force_authenticate(user=self.admin)
        self.address = _make_address()
        self.user = _make_user()

    def test_returns_12_months(self):
        resp = self.client.get('/revenue/monthly/', {'year': 2025})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 12)
        months = [d['month'] for d in resp.data]
        self.assertEqual(months, list(range(1, 13)))

    def test_recibidos_sum_correct(self):
        _make_order(self.address, self.user, 'payment_confirmed', 2025, 3, price=500, qty=2)
        _make_order(self.address, self.user, 'delivered', 2025, 3, price=300, qty=1)
        resp = self.client.get('/revenue/monthly/', {'year': 2025})
        march = next(d for d in resp.data if d['month'] == 3)
        self.assertEqual(float(march['recibidos']), 1300.0)
        self.assertEqual(float(march['pendientes']), 0.0)

    def test_pendientes_sum_correct(self):
        _make_order(self.address, self.user, 'pending', 2025, 5, price=200, qty=3)
        resp = self.client.get('/revenue/monthly/', {'year': 2025})
        may = next(d for d in resp.data if d['month'] == 5)
        self.assertEqual(float(may['pendientes']), 600.0)

    def test_excluidos_not_counted(self):
        _make_order(self.address, self.user, 'canceled', 2025, 7, price=999, qty=1)
        resp = self.client.get('/revenue/monthly/', {'year': 2025})
        july = next(d for d in resp.data if d['month'] == 7)
        self.assertEqual(float(july['recibidos']), 0.0)
        self.assertEqual(float(july['pendientes']), 0.0)

    def test_empty_months_return_zero(self):
        resp = self.client.get('/revenue/monthly/', {'year': 2099})
        for d in resp.data:
            self.assertEqual(float(d['recibidos']), 0.0)
            self.assertEqual(float(d['pendientes']), 0.0)

    def test_requires_admin(self):
        regular = _make_user('regular@t.com')
        self.client.force_authenticate(user=regular)
        resp = self.client.get('/revenue/monthly/', {'year': 2025})
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

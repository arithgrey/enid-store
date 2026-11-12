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
from revenue.tests.test_monthly import _make_address, _make_user, _make_order


class SummaryRevenueTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser('admin@t.com', 'admin@t.com', 'pass')
        self.client.force_authenticate(user=self.admin)
        self.address = _make_address()
        self.user = _make_user()

    def test_summary_recibidos_and_pendientes(self):
        _make_order(self.address, self.user, 'payment_confirmed', 2025, 4, price=400, qty=2)
        _make_order(self.address, self.user, 'pending', 2025, 4, price=100, qty=3)
        resp = self.client.get('/revenue/summary/', {'year': 2025, 'month': 4})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(float(resp.data['recibidos']), 800.0)
        self.assertEqual(float(resp.data['pendientes']), 300.0)
        self.assertEqual(float(resp.data['total']), 1100.0)

    def test_summary_total_equals_sum(self):
        _make_order(self.address, self.user, 'delivered', 2025, 6, price=250, qty=1)
        resp = self.client.get('/revenue/summary/', {'year': 2025, 'month': 6})
        self.assertAlmostEqual(
            float(resp.data['total']),
            float(resp.data['recibidos']) + float(resp.data['pendientes'])
        )

    def test_summary_excludes_canceled(self):
        _make_order(self.address, self.user, 'canceled', 2025, 8, price=999, qty=1)
        resp = self.client.get('/revenue/summary/', {'year': 2025, 'month': 8})
        self.assertEqual(float(resp.data['total']), 0.0)

    def test_summary_empty_month_returns_zeros(self):
        resp = self.client.get('/revenue/summary/', {'year': 2099, 'month': 1})
        self.assertEqual(float(resp.data['recibidos']), 0.0)
        self.assertEqual(float(resp.data['pendientes']), 0.0)
        self.assertEqual(float(resp.data['total']), 0.0)

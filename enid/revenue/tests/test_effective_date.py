from datetime import datetime
import pytz
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from order.models import Order
from item_order.models import ItemOrder
from revenue.tests.test_monthly import _make_address, _make_product

User = get_user_model()


class EffectiveDateRevenueTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser('a@t.com', 'a@t.com', 'pass')
        self.client.force_authenticate(user=self.admin)
        self.address = _make_address()

    def _order_with_sale_date(self, created_year, created_month, sale_year, sale_month):
        created = datetime(created_year, created_month, 15, 12, 0, tzinfo=pytz.UTC)
        sale = datetime(sale_year, sale_month, 15, 12, 0, tzinfo=pytz.UTC)
        order = Order.objects.create(shipping_address=self.address, status='delivered')
        Order.objects.filter(pk=order.pk).update(created_at=created, sale_date=sale)
        ItemOrder.objects.create(order=order, product=_make_product(), quantity=1, price=500)
        return order

    def test_sale_date_overrides_created_at_in_summary(self):
        # Orden creada en enero pero vendida (histórica) en abril → cuenta en abril.
        self._order_with_sale_date(2025, 1, 2025, 4)
        resp = self.client.get('/revenue/summary/', {'year': 2025, 'month': 4})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(float(resp.data['recibidos']), 500.0)

    def test_null_sale_date_falls_back_to_created_at(self):
        # Sin sale_date → se usa created_at (no regresión).
        order = Order.objects.create(shipping_address=self.address, status='delivered')
        created = datetime(2025, 7, 10, 12, 0, tzinfo=pytz.UTC)
        Order.objects.filter(pk=order.pk).update(created_at=created)
        ItemOrder.objects.create(order=order, product=_make_product(), quantity=1, price=300)
        resp = self.client.get('/revenue/summary/', {'year': 2025, 'month': 7})
        self.assertEqual(float(resp.data['recibidos']), 300.0)

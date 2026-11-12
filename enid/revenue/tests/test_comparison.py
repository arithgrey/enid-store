from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from revenue.tests.test_monthly import _make_address, _make_user, _make_order


class ComparisonRevenueTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser('admin@t.com', 'admin@t.com', 'pass')
        self.client.force_authenticate(user=self.admin)
        self.address = _make_address()
        self.user = _make_user()

    def test_returns_12_months(self):
        resp = self.client.get('/revenue/comparison/', {'year': 2025})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 12)

    def test_current_year_data_correct(self):
        _make_order(self.address, self.user, 'payment_confirmed', 2025, 3, price=1000, qty=1)
        resp = self.client.get('/revenue/comparison/', {'year': 2025})
        march = next(d for d in resp.data if d['month'] == 3)
        self.assertEqual(float(march['current']), 1000.0)

    def test_previous_year_data_correct(self):
        _make_order(self.address, self.user, 'delivered', 2024, 3, price=500, qty=2)
        resp = self.client.get('/revenue/comparison/', {'year': 2025})
        march = next(d for d in resp.data if d['month'] == 3)
        self.assertEqual(float(march['previous']), 1000.0)

    def test_future_months_current_year_are_null(self):
        """Meses futuros del año actual devuelven null para current."""
        import datetime
        from django.utils import timezone
        current_month = timezone.now().month
        current_year = timezone.now().year
        resp = self.client.get('/revenue/comparison/', {'year': current_year})
        for d in resp.data:
            if d['month'] > current_month:
                self.assertIsNone(d['current'], f"month {d['month']} should be null")

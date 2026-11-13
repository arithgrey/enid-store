from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from products.models import Product
from order.models import Order

User = get_user_model()


def _make_product():
    # Reusamos un producto sembrado (post_migrate) para evitar colisiones con la
    # secuencia de Postgres, mismo patrón que test_auto_candidate.py / Task 5.
    p = Product.objects.first()
    p.certification = 'published'
    p.certified_at = None
    p.save(update_fields=['certification', 'certified_at'])
    return p


class ManualSaleTest(TestCase):
    URL = '/productos/manual-sale/'

    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser('ms@t.com', 'ms@t.com', 'pass')

    def test_manual_sale_with_historical_date_counts_and_promotes(self):
        self.client.force_authenticate(user=self.admin)
        product = _make_product()
        payload = {
            'items': [{'product': product.id, 'quantity': 2, 'price': 250}],
            'status': 'delivered',
            'sale_date': '2025-03-15T12:00:00Z',
        }
        resp = self.client.post(self.URL, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        # Orden creada como manual
        order = Order.objects.get(pk=resp.data['order_id'])
        self.assertEqual(order.source, 'admin_manual')
        self.assertIsNotNone(order.sale_date)
        # Producto promovido a candidate por el signal
        product.refresh_from_db()
        self.assertEqual(product.certification, 'candidate')
        # Cuenta en revenue en marzo 2025 (fecha efectiva = sale_date)
        summary = self.client.get('/revenue/summary/', {'year': 2025, 'month': 3})
        self.assertEqual(float(summary.data['recibidos']), 500.0)

    def test_no_items_returns_400(self):
        self.client.force_authenticate(user=self.admin)
        resp = self.client.post(self.URL, {'items': [], 'status': 'delivered'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_nonexistent_product_returns_400(self):
        self.client.force_authenticate(user=self.admin)
        payload = {'items': [{'product': 999999, 'quantity': 1, 'price': 10}], 'status': 'delivered'}
        resp = self.client.post(self.URL, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_status_returns_400(self):
        self.client.force_authenticate(user=self.admin)
        product = _make_product()
        payload = {'items': [{'product': product.id, 'quantity': 1, 'price': 10}], 'status': 'pending'}
        resp = self.client.post(self.URL, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_non_admin_returns_403(self):
        plain = User.objects.create_user('u2@t.com', 'u2@t.com', 'pass')
        self.client.force_authenticate(user=plain)
        product = _make_product()
        payload = {'items': [{'product': product.id, 'quantity': 1, 'price': 10}], 'status': 'delivered'}
        resp = self.client.post(self.URL, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

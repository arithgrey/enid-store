from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()


def _make_product(certification='candidate'):
    # Reusamos un producto sembrado (post_migrate) para evitar colisiones con la
    # secuencia de Postgres, mismo patrón que test_auto_candidate.py.
    p = Product.objects.first()
    p.certification = certification
    p.certified_at = None
    p.save(update_fields=['certification', 'certified_at'])
    return p


class CertificationEndpointTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser('ad@t.com', 'ad@t.com', 'pass')

    def _url(self, pk):
        return f'/productos/{pk}/certification/'

    def test_admin_confirms_candidate_to_certified(self):
        self.client.force_authenticate(user=self.admin)
        product = _make_product('candidate')
        resp = self.client.patch(self._url(product.id), {'certification': 'certified'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.certification, 'certified')
        self.assertIsNotNone(product.certified_at)

    def test_override_published_to_certified(self):
        self.client.force_authenticate(user=self.admin)
        product = _make_product('published')
        resp = self.client.patch(self._url(product.id), {'certification': 'certified'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.certification, 'certified')

    def test_revert_certified_clears_certified_at(self):
        self.client.force_authenticate(user=self.admin)
        product = _make_product('candidate')
        self.client.patch(self._url(product.id), {'certification': 'certified'}, format='json')
        resp = self.client.patch(self._url(product.id), {'certification': 'candidate'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.certification, 'candidate')
        self.assertIsNone(product.certified_at)

    def test_invalid_state_returns_400(self):
        self.client.force_authenticate(user=self.admin)
        product = _make_product('published')
        resp = self.client.patch(self._url(product.id), {'certification': 'xxx'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_non_admin_returns_403(self):
        plain = User.objects.create_user('u@t.com', 'u@t.com', 'pass')
        self.client.force_authenticate(user=plain)
        product = _make_product('candidate')
        resp = self.client.patch(self._url(product.id), {'certification': 'certified'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

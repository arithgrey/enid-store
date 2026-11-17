from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from order.models import Order
from address.models import Address
from state.models import State

User = get_user_model()

URL = '/productos/clientes/'


def _make_state():
    return State.objects.first()


def _make_address(state):
    return Address.objects.create(
        street='Av. Hidalgo',
        number=10,
        interior_number=1,
        colony='Centro',
        delegation_or_municipality='Cuauhtémoc',
        city='CDMX',
        postal_code='06600',
        phone_number='5512345678',
        state=state,
    )


class ClientSearchTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser('admin@t.com', 'admin@t.com', 'pass')

    def test_search_by_email_returns_client_with_last_address(self):
        state = _make_state()
        addr = _make_address(state)
        user = User.objects.create_user('ana@ejemplo.com', 'ana@ejemplo.com', 'pass',
                                        first_name='Ana', last_name='García')
        Order.objects.create(status='delivered', source='admin_manual', shipping_address=addr, user=user)

        self.client.force_authenticate(user=self.admin)
        resp = self.client.get(URL, {'q': 'ana@ejemplo.com'})

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data[0]['id'], user.id)
        self.assertEqual(resp.data[0]['email'], 'ana@ejemplo.com')
        self.assertEqual(resp.data[0]['name'], 'Ana García')
        self.assertEqual(resp.data[0]['last_address']['street'], 'Av. Hidalgo')
        self.assertEqual(resp.data[0]['last_address']['postal_code'], '06600')

    def test_search_by_partial_name_returns_matches(self):
        User.objects.create_user('luis@t.com', 'luis@t.com', 'pass',
                                 first_name='Luis', last_name='Pérez')
        User.objects.create_user('otro@t.com', 'otro@t.com', 'pass',
                                 first_name='Carlos', last_name='Ramírez')

        self.client.force_authenticate(user=self.admin)
        resp = self.client.get(URL, {'q': 'Luis'})

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        names = [r['name'] for r in resp.data]
        self.assertIn('Luis Pérez', names)
        self.assertNotIn('Carlos Ramírez', names)

    def test_empty_query_returns_400(self):
        self.client.force_authenticate(user=self.admin)
        resp = self.client.get(URL, {'q': ''})
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_query_param_returns_400(self):
        self.client.force_authenticate(user=self.admin)
        resp = self.client.get(URL)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_results_returns_empty_list(self):
        self.client.force_authenticate(user=self.admin)
        resp = self.client.get(URL, {'q': 'zzznoresult'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, [])

    def test_user_without_orders_has_null_last_address(self):
        User.objects.create_user('solo@t.com', 'solo@t.com', 'pass',
                                 first_name='Solo', last_name='User')
        self.client.force_authenticate(user=self.admin)
        resp = self.client.get(URL, {'q': 'solo@t.com'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIsNone(resp.data[0]['last_address'])

    def test_non_admin_returns_403(self):
        plain = User.objects.create_user('plain@t.com', 'plain@t.com', 'pass')
        self.client.force_authenticate(user=plain)
        resp = self.client.get(URL, {'q': 'algo'})
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

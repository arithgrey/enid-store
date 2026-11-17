from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from order.models import Order
from address.models import Address
from state.models import State
from products.models import Product

User = get_user_model()
URL = '/productos/manual-sale/'


def _make_product():
    p = Product.objects.first()
    p.certification = 'published'
    p.certified_at = None
    p.save(update_fields=['certification', 'certified_at'])
    return p


def _base_payload(product):
    return {
        'items': [{'product': product.id, 'quantity': 1, 'price': 100}],
        'status': 'delivered',
    }


def _address_payload():
    state = State.objects.first()
    return {
        'street': 'Calle Morelos',
        'number': 5,
        'interior_number': 1,
        'colony': 'Juárez',
        'delegation_or_municipality': 'Cuauhtémoc',
        'city': 'CDMX',
        'state': state.id,
        'postal_code': '06600',
        'phone_number': '5598765432',
        'additional_details': '',
    }


class ManualSaleCustomerTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser('admin@ms.com', 'admin@ms.com', 'pass')
        self.client.force_authenticate(user=self.admin)

    def test_sale_with_customer_id_assigns_user(self):
        product = _make_product()
        user = User.objects.create_user('existing@t.com', 'existing@t.com', 'pass')
        payload = {**_base_payload(product), 'customer_id': user.id}

        resp = self.client.post(URL, payload, format='json')

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        order = Order.objects.get(pk=resp.data['order_id'])
        self.assertEqual(order.user_id, user.id)
        self.assertEqual(resp.data['customer_id'], user.id)
        self.assertEqual(resp.data['customer_email'], user.email)

    def test_sale_with_nonexistent_customer_id_returns_400(self):
        product = _make_product()
        payload = {**_base_payload(product), 'customer_id': 999999}

        resp = self.client.post(URL, payload, format='json')

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_sale_with_new_email_creates_user_and_assigns(self):
        product = _make_product()
        payload = {
            **_base_payload(product),
            'customer_email': 'nuevo@t.com',
            'customer_name': 'Luis Pérez',
        }

        resp = self.client.post(URL, payload, format='json')

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email='nuevo@t.com')
        self.assertEqual(user.first_name, 'Luis')
        self.assertEqual(user.last_name, 'Pérez')
        order = Order.objects.get(pk=resp.data['order_id'])
        self.assertEqual(order.user_id, user.id)

    def test_sale_with_existing_email_reuses_user(self):
        product = _make_product()
        existing = User.objects.create_user('reuse@t.com', 'reuse@t.com', 'pass')
        payload = {**_base_payload(product), 'customer_email': 'reuse@t.com'}

        resp = self.client.post(URL, payload, format='json')

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        order = Order.objects.get(pk=resp.data['order_id'])
        self.assertEqual(order.user_id, existing.id)
        self.assertEqual(User.objects.filter(email='reuse@t.com').count(), 1)

    def test_sale_with_empty_customer_email_returns_400(self):
        product = _make_product()
        payload = {**_base_payload(product), 'customer_email': ''}

        resp = self.client.post(URL, payload, format='json')

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_sale_with_address_creates_and_assigns_shipping_address(self):
        product = _make_product()
        payload = {**_base_payload(product), 'address': _address_payload()}

        resp = self.client.post(URL, payload, format='json')

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        order = Order.objects.get(pk=resp.data['order_id'])
        self.assertIsNotNone(order.shipping_address)
        self.assertEqual(order.shipping_address.street, 'Calle Morelos')
        self.assertEqual(order.shipping_address.postal_code, '06600')

    def test_sale_without_customer_or_address_is_retrocompatible(self):
        product = _make_product()

        resp = self.client.post(URL, _base_payload(product), format='json')

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        order = Order.objects.get(pk=resp.data['order_id'])
        self.assertIsNone(order.user)
        self.assertIsNone(order.shipping_address)

    def test_sale_with_address_missing_required_field_returns_400(self):
        product = _make_product()
        addr = _address_payload()
        del addr['street']
        payload = {**_base_payload(product), 'address': addr}

        resp = self.client.post(URL, payload, format='json')

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

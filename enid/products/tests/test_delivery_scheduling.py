from django.test import TestCase
from products.models import Product
from order.models import Order
from rest_framework.test import APIClient
from products.models import PaymentMethod
from categories.models import Category
from address.models import Address
from state.models import State


class DeliverySchedulingModelTest(TestCase):

    def test_product_has_allows_scheduled_delivery_field(self):
        field = Product._meta.get_field('allows_scheduled_delivery')
        self.assertEqual(field.get_internal_type(), 'BooleanField')
        self.assertFalse(field.default)

    def test_product_has_is_service_field(self):
        field = Product._meta.get_field('is_service')
        self.assertEqual(field.get_internal_type(), 'BooleanField')
        self.assertFalse(field.default)

    def test_product_has_min_delivery_days_field(self):
        field = Product._meta.get_field('min_delivery_days')
        self.assertEqual(field.get_internal_type(), 'PositiveIntegerField')
        self.assertEqual(field.default, 1)

    def test_product_scheduling_fields_in_meta(self):
        field_names = [f.name for f in Product._meta.fields]
        self.assertIn('allows_scheduled_delivery', field_names)
        self.assertIn('is_service', field_names)
        self.assertIn('min_delivery_days', field_names)

    def test_order_has_delivery_date_end_field(self):
        field = Order._meta.get_field('delivery_date_end')
        self.assertEqual(field.get_internal_type(), 'DateField')
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_order_delivery_date_end_in_meta(self):
        field_names = [f.name for f in Order._meta.fields]
        self.assertIn('delivery_date_end', field_names)


class PODOrderDeliveryDateTest(TestCase):

    def setUp(self):
        from django.db import connection
        self.client = APIClient()
        self.category = Category.objects.first() or Category.objects.create(
            name='Test', slug='test'
        )
        self.state = State.objects.first() or State.objects.create(name='Test State', code='TS')
        PaymentMethod.objects.get_or_create(slug='contra_entrega', defaults={'name': 'Paga al recibir'})
        # Reset sequence to avoid PK conflicts with seed data
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT setval(pg_get_serial_sequence('products_product', 'id'), "
                "(SELECT COALESCE(MAX(id), 0) FROM products_product) + 1, false)"
            )

    def _base_payload(self, product):
        return {
            "name": "Test Cliente",
            "phone_number": "5512345678",
            "street": "Calle Falsa 123",
            "state": self.state.id,
            "products": [{"id": product.id, "quantity": 1, **self._product_dict(product)}]
        }

    def _product_dict(self, product):
        return {
            "name": product.name,
            "price": str(product.price),
            "allows_scheduled_delivery": product.allows_scheduled_delivery,
            "is_service": product.is_service,
            "payment_methods": list(product.payment_methods.values_list('slug', flat=True))
        }

    def test_order_with_scheduling_requires_delivery_date(self):
        product = Product.objects.create(
            name='P1', specific_name='P1', price=100, category=self.category,
            allows_scheduled_delivery=True
        )
        payload = self._base_payload(product)
        response = self.client.post('/order-payment-on-delivery/pod/', payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('delivery_date', str(response.data))

    def test_order_service_requires_delivery_date_end(self):
        product = Product.objects.create(
            name='P2', specific_name='P2', price=100, category=self.category,
            allows_scheduled_delivery=True, is_service=True
        )
        payload = self._base_payload(product)
        payload['delivery_date'] = '2027-01-15'
        response = self.client.post('/order-payment-on-delivery/pod/', payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('delivery_date_end', str(response.data))

    def test_order_with_valid_delivery_date_saves_it(self):
        product = Product.objects.create(
            name='P3', specific_name='P3', price=100, category=self.category,
            allows_scheduled_delivery=True
        )
        payload = self._base_payload(product)
        payload['delivery_date'] = '2027-01-15'
        response = self.client.post('/order-payment-on-delivery/pod/', payload, format='json')
        self.assertEqual(response.status_code, 201)
        from order.models import Order
        order = Order.objects.get(id=response.data['id'])
        self.assertEqual(str(order.delivery_date.date()), '2027-01-15')

    def test_order_service_with_valid_range_saves_both_dates(self):
        product = Product.objects.create(
            name='P4', specific_name='P4', price=100, category=self.category,
            allows_scheduled_delivery=True, is_service=True
        )
        payload = self._base_payload(product)
        payload['delivery_date'] = '2027-02-01'
        payload['delivery_date_end'] = '2027-02-28'
        response = self.client.post('/order-payment-on-delivery/pod/', payload, format='json')
        self.assertEqual(response.status_code, 201)
        from order.models import Order
        order = Order.objects.get(id=response.data['id'])
        from datetime import date
        self.assertEqual(order.delivery_date_end, date(2027, 2, 28))

    def test_delivery_date_end_before_start_returns_400(self):
        product = Product.objects.create(
            name='P5', specific_name='P5', price=100, category=self.category,
            allows_scheduled_delivery=True, is_service=True
        )
        payload = self._base_payload(product)
        payload['delivery_date'] = '2027-02-28'
        payload['delivery_date_end'] = '2027-02-01'
        response = self.client.post('/order-payment-on-delivery/pod/', payload, format='json')
        self.assertEqual(response.status_code, 400)

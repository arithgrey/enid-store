from django.test import TestCase
from products.models import Product
from order.models import Order


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

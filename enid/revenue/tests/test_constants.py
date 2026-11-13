from django.test import TestCase
from revenue.constants import RECIBIDOS, PENDIENTES, ALL_COUNTED


class RevenueConstantsTest(TestCase):
    def test_recibidos_values(self):
        self.assertEqual(
            RECIBIDOS, ['payment_confirmed', 'delivered', 'cash_on_delivery']
        )

    def test_pendientes_values(self):
        self.assertEqual(
            PENDIENTES,
            ['pending', 'preparing', 'ready_for_shipping', 'in_transit', 'ready_for_pickup'],
        )

    def test_all_counted_is_union(self):
        self.assertEqual(ALL_COUNTED, RECIBIDOS + PENDIENTES)

"""
Seed de datos demo para verificar el dashboard de ingresos.

Genera órdenes con status mixtos (recibidos/pendientes) distribuidas en
varios meses de los años actual y anterior, para poder comprobar que los
4 endpoints de revenue (monthly, summary, comparison, by-product)
devuelven agregaciones reales.

Idempotente: marca las órdenes creadas con source='revenue_demo_seed' y
las borra antes de volver a sembrar.

    docker exec enid_store_service python manage.py seed_revenue_demo
    docker exec enid_store_service python manage.py seed_revenue_demo --clear
"""
from datetime import datetime, timezone as dt_timezone
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from order.models import Order
from item_order.models import ItemOrder
from products.models import Product
from revenue.constants import RECIBIDOS, PENDIENTES

SEED_SOURCE = "revenue_demo_seed"

# (mes, status, [(product_index, quantity), ...])
# product_index indexa la lista ordenada de productos disponibles.
CURRENT_YEAR_PLAN = [
    (1,  "delivered",         [(0, 1)]),
    (2,  "payment_confirmed", [(1, 2)]),
    (3,  "delivered",         [(2, 1), (0, 1)]),
    (4,  "cash_on_delivery",  [(3, 1)]),
    (5,  "delivered",         [(1, 1)]),
    (6,  "payment_confirmed", [(4, 2)]),
    (7,  "delivered",         [(2, 1)]),
    (8,  "cash_on_delivery",  [(0, 3)]),
    (9,  "delivered",         [(5, 1), (1, 1)]),
    (10, "payment_confirmed", [(3, 2)]),
    # mes actual sembrado aparte (abajo) para garantizar recibidos + pendientes + varios productos
]

PREVIOUS_YEAR_PLAN = [
    (2,  "delivered",         [(0, 1)]),
    (5,  "payment_confirmed", [(1, 1)]),
    (8,  "cash_on_delivery",  [(2, 2)]),
    (11, "delivered",         [(3, 1)]),
]


class Command(BaseCommand):
    help = "Seed de órdenes demo para verificar el dashboard de ingresos"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Solo borra el seed previo, sin volver a sembrar.",
        )

    def _clear(self):
        qs = Order.objects.filter(source=SEED_SOURCE)
        n = qs.count()
        qs.delete()  # cascade borra los ItemOrder
        self.stdout.write(f"Borradas {n} órdenes de seed previas.")

    def _make_order(self, year, month, status, lines, products):
        order = Order.objects.create(status=status, source=SEED_SOURCE)
        for idx, qty in lines:
            product = products[idx % len(products)]
            ItemOrder.objects.create(
                order=order,
                product=product,
                quantity=qty,
                price=product.price,
            )
        # created_at es auto_now_add -> hay que forzarlo con update()
        dt = datetime(year, month, 15, 12, 0, 0, tzinfo=dt_timezone.utc)
        Order.objects.filter(pk=order.pk).update(created_at=dt)
        return order

    @transaction.atomic
    def handle(self, *args, **options):
        self._clear()
        if options["clear"]:
            return

        products = list(Product.objects.order_by("id")[:6])
        if len(products) < 6:
            self.stderr.write("Se necesitan al menos 6 productos para el seed.")
            return

        now = timezone.now()
        created = 0

        # Año actual, meses 1..10
        for month, status, lines in CURRENT_YEAR_PLAN:
            self._make_order(now.year, month, status, lines, products)
            created += 1

        # Mes actual: recibidos + pendientes + varios productos (para by-product)
        current_month_plan = [
            ("delivered",         [(0, 2), (1, 1)]),
            ("payment_confirmed", [(2, 1)]),
            ("cash_on_delivery",  [(3, 1)]),
            ("pending",           [(4, 2)]),
            ("in_transit",        [(5, 1)]),
            ("preparing",         [(1, 1)]),
        ]
        for status, lines in current_month_plan:
            self._make_order(now.year, now.month, status, lines, products)
            created += 1

        # Año anterior (para comparison)
        for month, status, lines in PREVIOUS_YEAR_PLAN:
            self._make_order(now.year - 1, month, status, lines, products)
            created += 1

        self.stdout.write(self.style.SUCCESS(f"Seed completo: {created} órdenes demo creadas."))

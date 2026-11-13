"""Fuente única de verdad de los estados de orden que cuentan como ingreso.

WHY: estas listas estaban duplicadas en views.py, seed_revenue_demo.py y los
tests. La regla "genera ingreso" (RECIBIDOS) la consume también la máquina de
certificación de productos, así que vive en un solo lugar.
"""

RECIBIDOS = ['payment_confirmed', 'delivered', 'cash_on_delivery']
PENDIENTES = ['pending', 'preparing', 'ready_for_shipping', 'in_transit', 'ready_for_pickup']
ALL_COUNTED = RECIBIDOS + PENDIENTES

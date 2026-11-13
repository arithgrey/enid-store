#Servicio par agregar productos al carro de compras (Ver implementaciones en product_cart.py)
class ServiceProductCart:
    def __init__(self, product_cart_handler):
        self.product_cart_handler = product_cart_handler

    def add_product(self, cart, product, amount):
        self.product_cart_handler.add_product(cart, product, amount)


def promote_products_to_candidate(order):
    """Promueve a 'candidate' los productos 'published' de una orden con ingreso real.

    Idempotente: el filtro certification='published' deja intactos los productos
    ya 'candidate' o 'certified' (una venta posterior nunca degrada un certified).
    """
    # Import local para evitar ciclo de import en apps.ready / signals.
    from revenue.constants import RECIBIDOS
    from products.models import Product

    if order.status not in RECIBIDOS:
        return
    product_ids = list(order.items.values_list('product_id', flat=True))
    if not product_ids:
        return
    Product.objects.filter(
        id__in=product_ids, certification='published'
    ).update(certification='candidate')
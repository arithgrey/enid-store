import logging
import requests
from django.conf import settings

logger = logging.getLogger(__name__)


def notify_order(event: str, order) -> None:
    url = getattr(settings, "NOTIFICATIONS_SERVICE_URL", "")
    if not url:
        return

    items = order.items.select_related("product").all()
    products = [f"{item.product.name} x{item.quantity}" for item in items]
    total = float(sum(item.price * item.quantity for item in items))

    user = order.user
    if user and (user.first_name or user.last_name):
        client_name = f"{user.first_name} {user.last_name}".strip()
    else:
        client_name = "Cliente"

    payload = {
        "event": event,
        "order_id": order.id,
        "client_name": client_name,
        "total": total,
        "products": products,
        "source": order.source or "",
    }

    try:
        requests.post(
            f"{url}/notify/order",
            json=payload,
            timeout=3,
        )
    except Exception as e:
        logger.error("notify_order failed for order %s: %s", order.id, e)

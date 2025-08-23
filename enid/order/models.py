from django.db import models
from django.contrib.auth.models import User
from address.models import Address
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pedido recibido'),                 # Pedido recibido, pero no procesado
        ('payment_confirmed', 'Pago Confirmado'), # Pago recibido y confirmado
        ('preparing', 'Preparando'),       # Pedido en preparación
        ('ready_for_shipping', 'Listo para Envío'), # Listo para ser recogido por la mensajería
        ('in_transit', 'En Tránsito ...'),            # Pedido en camino al cliente
        ('ready_for_pickup', 'Listo para Recoger'),# Listo para ser recogido por el cliente
        ('delivered', 'Entregado'),               # Pedido entregado exitosamente
        ('returned', 'Devuelto'),                 # Pedido devuelto por el cliente
        ('refund_processed', 'Reembolso Procesado'), # Reembolso emitido
        ('canceled', 'Cancelada'),                # Pedido cancelado
        ('cash_on_delivery', 'Pagado contra Entrega') # Pago al recibir
    )
    
    CLIENT_VISIBLE_STATUSES = {'pending', 'preparing','in_transit', 'delivered'}
    ADMIN_TIMELINE_VISIBLE_STATUSES = {'pending','payment_confirmed', 'preparing','ready_for_shipping','in_transit', 'delivered'}
    
    shipping_address = models.ForeignKey(Address, related_name='order_address', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')        
    user = models.ForeignKey(User, related_name='user_order', on_delete=models.CASCADE, null=True, blank=True)
    payment_on_delivery = models.BooleanField(default=False)
    source = models.CharField(max_length=200, blank=True, null=True, help_text="Landing page o fuente de origen de la orden")
    
    def __str__(self):
        return f"Order {self.id}"
    

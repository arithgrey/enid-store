from django.db import models
from products.models import Product

class ProductComponent(models.Model):
    kit = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='component_quantities'
    )
    component = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='kit_quantities'
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['kit', 'component']
        app_label = 'primary_components'

    def __str__(self):
        return f"{self.component.name} x{self.quantity} en {self.kit.name}"
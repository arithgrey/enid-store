from django.apps import AppConfig


class ProductVariantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_variant'
    def ready(self):
        import product_variant.signals

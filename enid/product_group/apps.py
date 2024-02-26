from django.apps import AppConfig


class ProductGroupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_group'
    
    def ready(self):
        import product_group.signals
    

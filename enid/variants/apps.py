from django.apps import AppConfig


class VariantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'variants'
    def ready(self):
        import variants.signals

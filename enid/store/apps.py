from django.apps import AppConfig


class StorerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'
    def ready(self):
        import store.signals

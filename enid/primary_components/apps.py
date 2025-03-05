from django.apps import AppConfig


class PrimaryComponentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'primary_components'

    def ready(self):
        import primary_components.signals

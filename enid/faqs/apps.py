from django.apps import AppConfig


class FaqsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'faqs'
    def ready(self):
        import faqs.signals

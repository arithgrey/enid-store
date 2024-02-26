from django.apps import AppConfig


class LeadTypeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lead_type'
    
    def ready(self):
        import lead_type.signals
    

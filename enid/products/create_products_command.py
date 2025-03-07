from django.core.management.base import BaseCommand
from django.apps import apps
from products.signals import create_products
import os

class Command(BaseCommand):
    help = 'Crea productos iniciales'

    def handle(self, *args, **options):
        os.environ['DJANGO_RUNNING_MIGRATIONS'] = 'True'
        sender = apps.get_app_config('products')
        create_products(sender)
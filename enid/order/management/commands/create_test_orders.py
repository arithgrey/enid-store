from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from order.models import Order
from address.models import Address
from state.models import State
from django.contrib.auth.models import User
import random


class Command(BaseCommand):
    help = 'Crea órdenes de prueba con diferentes fechas de entrega para testing del calendario'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=30,
            help='Número de órdenes a crear (default: 30)'
        )
        parser.add_argument(
            '--clean',
            action='store_true',
            help='Elimina órdenes de prueba existentes antes de crear nuevas'
        )

    def handle(self, *args, **options):
        count = options['count']
        clean = options['clean']

        # Limpiar órdenes de prueba si se solicita
        if clean:
            test_user = User.objects.filter(username='test_seed_user').first()
            if test_user:
                deleted_count = Order.objects.filter(user=test_user).count()
                Order.objects.filter(user=test_user).delete()
                self.stdout.write(self.style.WARNING(f'Eliminadas {deleted_count} órdenes de prueba existentes'))

        # Obtener o crear estado
        state, _ = State.objects.get_or_create(
            name='CDMX',
            defaults={'name': 'CDMX'}
        )

        # Obtener o crear usuario de prueba
        user, created = User.objects.get_or_create(
            username='test_seed_user',
            defaults={
                'email': 'test@seed.com',
                'first_name': 'Test',
                'last_name': 'Seed'
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Usuario de prueba creado: {user.username}'))

        # Obtener o crear dirección
        address, created = Address.objects.get_or_create(
            postal_code='54321',
            number=999,
            defaults={
                'street': 'Calle de Prueba',
                'interior_number': 1,
                'colony': 'Colonia Seed',
                'delegation_or_municipality': 'Delegación Test',
                'city': 'CDMX',
                'state': state,
                'phone_number': '5555555555'
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Dirección de prueba creada'))

        # Definir estados posibles para las órdenes
        statuses = ['pending', 'payment_confirmed', 'preparing', 'in_transit', 'delivered']

        # Crear órdenes con diferentes fechas
        today = timezone.now()
        created_count = 0

        self.stdout.write(self.style.SUCCESS(f'\nCreando {count} órdenes de prueba...'))

        for i in range(count):
            # Generar fecha aleatoria entre -30 y +30 días
            days_offset = random.randint(-30, 30)
            delivery_date = today + timedelta(days=days_offset)
            
            # Crear la orden
            order = Order.objects.create(
                shipping_address=address,
                user=user,
                delivery_date=delivery_date,
                status=random.choice(statuses)
            )
            
            created_count += 1
            
            # Mostrar progreso cada 10 órdenes
            if (i + 1) % 10 == 0:
                self.stdout.write(f'  Creadas {i + 1} órdenes...')

        # Crear algunas órdenes con delivery_date NULL para probar el fallback a created_at
        null_delivery_orders = 5
        self.stdout.write(self.style.WARNING(f'\nCreando {null_delivery_orders} órdenes sin delivery_date (usarán created_at)...'))
        
        for i in range(null_delivery_orders):
            order = Order.objects.create(
                shipping_address=address,
                user=user,
                status=random.choice(statuses)
            )
            # Forzar delivery_date a None
            Order.objects.filter(id=order.id).update(delivery_date=None)
            created_count += 1

        # Resumen
        self.stdout.write(self.style.SUCCESS(f'\n✅ Total de órdenes creadas: {created_count}'))
        self.stdout.write(self.style.SUCCESS(f'   - Con delivery_date: {count}'))
        self.stdout.write(self.style.SUCCESS(f'   - Sin delivery_date (NULL): {null_delivery_orders}'))
        
        # Estadísticas
        total_orders = Order.objects.filter(user=user).count()
        self.stdout.write(self.style.SUCCESS(f'\n📊 Total de órdenes del usuario de prueba: {total_orders}'))
        
        # Mostrar algunas órdenes de ejemplo
        self.stdout.write(self.style.SUCCESS('\n📋 Primeras 5 órdenes creadas:'))
        for order in Order.objects.filter(user=user).order_by('-created_at')[:5]:
            delivery = order.delivery_date.date() if order.delivery_date else order.created_at.date()
            self.stdout.write(f'   ID: {order.id} | Entrega: {delivery} | Estado: {order.status}') 
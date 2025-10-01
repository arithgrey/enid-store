from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from rest_framework.test import APIClient
from rest_framework import status
from order.models import Order
from address.models import Address
from state.models import State
from django.contrib.auth.models import User


class DeliveryStatsIntegrationTest(TestCase):
    """
    Tests de integración end-to-end para el endpoint de estadísticas de entregas
    Sin mocks - Solo pruebas reales con base de datos y API
    """

    def setUp(self):
        """Configurar datos reales de prueba"""
        self.client = APIClient()
        
        # Crear estado real
        self.state = State.objects.create(name="CDMX")
        
        # Crear usuario real
        self.user = User.objects.create(
            username='testuser@example.com',
            email='testuser@example.com',
            first_name='Test',
            last_name='User'
        )
        
        # Crear dirección real
        self.address = Address.objects.create(
            postal_code='12345',
            street='Calle Prueba',
            number=123,
            interior_number=1,
            colony='Colonia Test',
            delegation_or_municipality='Delegación Test',
            city='CDMX',
            state=self.state,
            phone_number='5551234567'
        )

    def test_delivery_stats_endpoint_returns_correct_data(self):
        """
        TDD: Verificar que el endpoint devuelve estadísticas correctas de entregas
        """
        # Arrange - Crear órdenes con diferentes delivery_dates
        today = timezone.now().date()
        tomorrow = today + timedelta(days=1)
        
        # 3 órdenes para hoy
        for i in range(3):
            Order.objects.create(
                shipping_address=self.address,
                user=self.user,
                delivery_date=timezone.now()
            )
        
        # 2 órdenes para mañana
        for i in range(2):
            Order.objects.create(
                shipping_address=self.address,
                user=self.user,
                delivery_date=timezone.now() + timedelta(days=1)
            )
        
        # Act - Llamar al endpoint
        response = self.client.get('/orden/delivery-stats/')
        
        # Assert - Verificar respuesta
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertIn('data', response.data)
        
        # Verificar conteos
        stats = response.data['data']
        today_str = today.strftime('%Y-%m-%d')
        tomorrow_str = tomorrow.strftime('%Y-%m-%d')
        
        self.assertEqual(stats[today_str], 3, "Debe haber 3 entregas para hoy")
        self.assertEqual(stats[tomorrow_str], 2, "Debe haber 2 entregas para mañana")

    def test_delivery_stats_with_date_range_filter(self):
        """
        TDD: Verificar que el endpoint filtra por rango de fechas
        """
        # Arrange - Crear órdenes en diferentes fechas
        today = timezone.now()
        yesterday = today - timedelta(days=2)  # 2 días atrás para asegurar distinción
        
        Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            delivery_date=yesterday
        )
        
        Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            delivery_date=today
        )
        
        # Act - Filtrar solo desde hoy en adelante
        today_str = today.date().strftime('%Y-%m-%d')
        response = self.client.get(f'/orden/delivery-stats/?start_date={today_str}')
        
        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        stats = response.data['data']
        # Debe incluir hoy pero no ayer
        self.assertIn(today_str, stats)
        yesterday_str = yesterday.date().strftime('%Y-%m-%d')
        self.assertNotIn(yesterday_str, stats)

    def test_delivery_stats_uses_created_at_when_delivery_date_is_null(self):
        """
        TDD: Verificar que el endpoint usa created_at cuando delivery_date es NULL
        """
        # Arrange - Crear orden sin delivery_date
        order_without_delivery_date = Order.objects.create(
            shipping_address=self.address,
            user=self.user
        )
        # Forzar delivery_date a None para simular órdenes antiguas
        Order.objects.filter(id=order_without_delivery_date.id).update(delivery_date=None)
        
        # Refrescar para obtener created_at
        order_without_delivery_date.refresh_from_db()
        
        # Crear orden con delivery_date
        order_with_delivery_date = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            delivery_date=timezone.now()
        )
        
        # Act
        response = self.client.get('/orden/delivery-stats/')
        
        # Assert - Debe contar AMBAS órdenes
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        stats = response.data['data']
        total_orders = sum(stats.values())
        self.assertEqual(total_orders, 2, "Debe contar todas las órdenes, usando created_at si delivery_date es NULL")
        
        # Verificar que la orden sin delivery_date aparece en su fecha de created_at
        created_date_key = order_without_delivery_date.created_at.date().strftime('%Y-%m-%d')
        self.assertIn(created_date_key, stats, "Debe usar created_at cuando delivery_date es NULL")

    def test_delivery_stats_empty_when_no_orders(self):
        """
        TDD: Verificar que el endpoint devuelve datos vacíos cuando no hay órdenes
        """
        # Act - No hay órdenes creadas
        response = self.client.get('/orden/delivery-stats/')
        
        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['data'], {})

    def test_delivery_stats_groups_by_date_not_time(self):
        """
        TDD: Verificar que las estadísticas agrupan por fecha, no por hora
        """
        # Arrange - Crear múltiples órdenes en el mismo día pero diferentes horas
        today = timezone.now()
        
        for hour in [8, 12, 18]:  # 3 diferentes horas del mismo día
            delivery_time = today.replace(hour=hour, minute=0, second=0)
            Order.objects.create(
                shipping_address=self.address,
                user=self.user,
                delivery_date=delivery_time
            )
        
        # Act
        response = self.client.get('/orden/delivery-stats/')
        
        # Assert - Todas deben estar agrupadas en el mismo día
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        stats = response.data['data']
        self.assertEqual(len(stats), 1, "Debe haber solo 1 entrada (un día)")
        
        today_str = today.date().strftime('%Y-%m-%d')
        self.assertEqual(stats[today_str], 3, "Las 3 órdenes deben estar en el mismo día") 
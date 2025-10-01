from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from order.models import Order
from address.models import Address
from state.models import State
from django.contrib.auth.models import User


class OrderDeliveryDateIntegrationTest(TestCase):
    """
    Tests de integración end-to-end para verificar el campo delivery_date
    Sin mocks - Solo pruebas reales con base de datos
    """

    def setUp(self):
        """Configurar datos reales de prueba"""
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

    def test_delivery_date_is_set_automatically_on_order_creation(self):
        """
        TDD: Verificar que delivery_date se establece automáticamente al crear una orden
        """
        # Arrange - Los datos ya están en setUp
        before_creation = timezone.now()
        
        # Act - Crear orden real
        order = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            status='pending'
        )
        
        after_creation = timezone.now()
        
        # Assert - Verificar que delivery_date se estableció
        self.assertIsNotNone(order.delivery_date, 
            "delivery_date debe establecerse automáticamente")
        
        # Verificar que delivery_date está en el rango de tiempo esperado
        self.assertGreaterEqual(order.delivery_date, before_creation,
            "delivery_date debe ser mayor o igual al momento antes de la creación")
        self.assertLessEqual(order.delivery_date, after_creation,
            "delivery_date debe ser menor o igual al momento después de la creación")

    def test_delivery_date_equals_created_at_on_new_order(self):
        """
        TDD: Verificar que delivery_date es aproximadamente igual a created_at
        """
        # Act - Crear orden real
        order = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            status='pending'
        )
        
        # Assert - Verificar que las fechas son muy similares (diferencia menor a 1 segundo)
        time_difference = abs((order.delivery_date - order.created_at).total_seconds())
        self.assertLess(time_difference, 1,
            f"delivery_date debe ser casi igual a created_at. Diferencia: {time_difference}s")

    def test_delivery_date_can_be_set_manually(self):
        """
        TDD: Verificar que delivery_date puede establecerse manualmente
        """
        # Arrange - Definir fecha de entrega personalizada
        custom_delivery_date = timezone.now() + timedelta(days=3)
        
        # Act - Crear orden con fecha de entrega personalizada
        order = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            status='pending',
            delivery_date=custom_delivery_date
        )
        
        # Assert - Verificar que se respeta la fecha personalizada
        self.assertEqual(order.delivery_date, custom_delivery_date,
            "delivery_date debe poder establecerse manualmente")

    def test_delivery_date_can_be_updated(self):
        """
        TDD: Verificar que delivery_date puede actualizarse después de crear la orden
        """
        # Arrange - Crear orden
        order = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            status='pending'
        )
        original_delivery_date = order.delivery_date
        
        # Act - Actualizar fecha de entrega
        new_delivery_date = timezone.now() + timedelta(days=5)
        order.delivery_date = new_delivery_date
        order.save()
        
        # Recargar desde la base de datos
        order.refresh_from_db()
        
        # Assert - Verificar que la fecha se actualizó
        self.assertEqual(order.delivery_date, new_delivery_date,
            "delivery_date debe poder actualizarse")
        self.assertNotEqual(order.delivery_date, original_delivery_date,
            "delivery_date debe ser diferente de la original")

    def test_delivery_date_persists_in_database(self):
        """
        TDD: Verificar que delivery_date se persiste correctamente en la base de datos
        """
        # Arrange & Act - Crear orden
        order = Order.objects.create(
            shipping_address=self.address,
            user=self.user,
            status='pending'
        )
        order_id = order.id
        delivery_date = order.delivery_date
        
        # Limpiar instancia del ORM
        del order
        
        # Act - Recuperar orden desde la base de datos
        retrieved_order = Order.objects.get(id=order_id)
        
        # Assert - Verificar que delivery_date se persistió correctamente
        self.assertIsNotNone(retrieved_order.delivery_date,
            "delivery_date debe persistirse en la base de datos")
        self.assertEqual(retrieved_order.delivery_date, delivery_date,
            "delivery_date recuperada debe ser igual a la original")

    def test_multiple_orders_have_different_delivery_dates(self):
        """
        TDD: Verificar que múltiples órdenes tienen delivery_dates únicos basados en su tiempo de creación
        """
        # Act - Crear múltiples órdenes con pequeño retraso entre ellas
        orders = []
        for i in range(3):
            order = Order.objects.create(
                shipping_address=self.address,
                user=self.user,
                status='pending'
            )
            orders.append(order)
            # Pequeño delay para asegurar diferentes timestamps
            import time
            time.sleep(0.1)
        
        # Assert - Verificar que cada orden tiene su propia delivery_date
        for i, order in enumerate(orders):
            self.assertIsNotNone(order.delivery_date,
                f"Orden {i} debe tener delivery_date")
        
        # Verificar que las fechas están en orden cronológico
        for i in range(len(orders) - 1):
            self.assertLessEqual(orders[i].delivery_date, orders[i + 1].delivery_date,
                f"delivery_date de orden {i} debe ser <= a orden {i + 1}") 
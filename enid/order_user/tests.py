from django.test import TestCase
from share_test.mixin import CommonMixinTest
from django.urls import reverse
from order.models import Order
from rest_framework import status
from share_test.oauth import OAuthUtilities
from share_test.orders import OrderCreationServiceHelper
from share_test.helpers.oauth_tests import OAuthTest
from django.contrib.auth.models import User


class TestUserOrderFilter(TestCase):
    def setUp(self):            
        super().setUp()
        self.api = '/order-user/'
        self.orderHelper = OrderCreationServiceHelper()
        self.oauthUtilities = OAuthUtilities()

    def test_filter_orders_by_user_email(self):
        """Test que valida el filtrado de órdenes por email del usuario"""
        # Crear usuario 1 con email específico y autenticar
        user1_email = "user1@test.com"
        user1, api_oauth_client = self.oauthUtilities.fake_user_and_api_client(
            username=user1_email,
            email=user1_email
        )
        
        # Crear usuario 2 con email diferente
        user2_email = "user2@test.com"
        user2 = self.orderHelper.crear_fake_user(
            username=user2_email,
            email=user2_email
        )
        
        # Crear 3 órdenes para user1
        orders_user1 = self.orderHelper.create_n_fake_orders(user=user1, total_orders=3)
        
        # Crear 2 órdenes para user2
        orders_user2 = self.orderHelper.create_n_fake_orders(user=user2, total_orders=2)
        
        # Verificar que se crearon correctamente
        self.assertEqual(len(orders_user1), 3)
        self.assertEqual(len(orders_user2), 2)
        
        # Hacer request filtrando por email de user1
        response = api_oauth_client.get(self.api, {"email": user1_email, "status": "pending"})
        
        # Verificar respuesta
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        
        # Verificar que todas las órdenes pertenecen al user1
        for order_data in response.data:
            order = Order.objects.get(id=order_data["id"])
            self.assertEqual(order.user.email, user1_email)
    
    def test_filter_orders_by_email_returns_empty_when_no_match(self):
        """Test que valida que retorna vacío cuando no hay órdenes con ese email"""
        # Crear usuario con email específico
        user_email = "existing@test.com"
        user, api_oauth_client = self.oauthUtilities.fake_user_and_api_client(
            username=user_email,
            email=user_email
        )
        
        # Crear órdenes para el usuario
        self.orderHelper.create_n_fake_orders(user=user, total_orders=2)
        
        # Buscar con un email que no existe
        non_existent_email = "nonexistent@test.com"
        response = api_oauth_client.get(self.api, {"email": non_existent_email, "status": "pending"})
        
        # Verificar que retorna OK pero sin resultados
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
    
    def test_filter_orders_by_email_combined_with_status(self):
        """Test que valida filtrado por email y status combinados"""
        # Crear usuario con email específico
        user_email = "combined@test.com"
        user, api_oauth_client = self.oauthUtilities.fake_user_and_api_client(
            username=user_email,
            email=user_email
        )
        
        # Crear órdenes con diferentes status
        pending_orders = self.orderHelper.create_n_fake_orders(
            user=user, total_orders=2, status='pending'
        )
        delivered_orders = self.orderHelper.create_n_fake_orders(
            user=user, total_orders=3, status='delivered'
        )
        
        # Filtrar por email y status=delivered
        response = api_oauth_client.get(self.api, {
            "email": user_email,
            "status": "delivered"
        })
        
        # Verificar que solo retorna las órdenes delivered
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        
        # Verificar que todas tienen status delivered
        for order_data in response.data:
            self.assertEqual(order_data["status"], "delivered")

#     def test_filter_order_by_user(self):
#         user, api_oauth_client  = self.oauthUtilities.fake_user_and_api_client()
#         order = self.orderHelper.create_fake_order_with_products(user=user)
            
#         self.assertIsInstance(order, Order)
#         order_id = order.id
        

#         filters = {
#             order.shipping_address.phone_number,                    
#             order_id,
#         }

#         for item in filters:
            
#             response = api_oauth_client.get(self.api, {"q":item})
#             order_by_request = response.data[0]               
#             self.assertEqual(response.status_code, status.HTTP_200_OK)
#             self.assertEqual(len(response.data),1)            
#             self.assertEqual(order_by_request["id"], order_id)


#     def test_filter_order_by_total(self):
        
#         user, api_oauth_client  = self.oauthUtilities.fake_user_and_api_client()
#         _ = self.orderHelper.create_n_fake_orders(total_orders=4)
#         fake_orders = self.orderHelper.create_n_fake_orders(
#             user=user, total_orders=10)        
        
        
#         self.assertEqual(len(fake_orders),10)
#         response = api_oauth_client.get(self.api)        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data),10)            

    
#     def test_filter_order_by_status(self):
                
#         user, api_oauth_client  = self.oauthUtilities.fake_user_and_api_client()
        
#         fake_orders_shipped = self.orderHelper.create_n_fake_orders(
#             user=user, total_orders=4, status='shipped')  
                
        
#         response = api_oauth_client.get(self.api,{'status':fake_orders_shipped[0].status})        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data),4)            
        


# class TestsUserAccessOrder(OAuthTest):    
#     '''Test validate accesss on order list'''
#     def setUp(self):             
#         super().setUp()                                
#         self.api = reverse("order_user:order-user") 
#         self.method  = 'get'test_unauthenticated_user

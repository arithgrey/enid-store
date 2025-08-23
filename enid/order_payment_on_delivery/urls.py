from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order_payment_on_delivery import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
app_name = 'order_payment_on_delivery'

router.register(r'', views.OrderPaymentOnDeliveryViewSet, basename="order_payment_on_delivery")

urlpatterns = router.urls
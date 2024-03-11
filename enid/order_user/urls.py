from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'order_user'

urlpatterns = [
    path('', views.OrderSearchViewSet.as_view({'get': 'search'}), name='order-user'),
]
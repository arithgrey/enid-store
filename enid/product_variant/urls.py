from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product_variant import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', views.ProducVariantVuewSet, basename="product-variant") #api crud de product_variant

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('producto/<int:product_id>/variantes/', views.ProductVariantByProductView.as_view(), name='product-variants'), #api busqueda de variantes por producto

]

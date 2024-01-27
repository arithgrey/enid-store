from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', views.ProductVuewSet, basename="product")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),  
    path('<str:category_slug>/<str:product_slug>/', views.ProductSlugVuewSet.as_view({'get':'get_by_slug'}), name='get_product_by_slug'),

]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from search import views

# Create a router and register our viewsets with it.
router = DefaultRouter()

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),  
    path('product/<str:q>/', views.ProductSeachByQViewSet.as_view({'get':'get_by_q'}), name='get_by_q'),

]
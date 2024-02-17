from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product_category_search import views

# Create a router and register our viewsets with it.
router = DefaultRouter()


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),      
    path('<str:category_slug>/', views.ProducByCategorySlugViewSet.as_view({'get':'get_by_category_slug'},name='get_by_category_slug')),
    
]   
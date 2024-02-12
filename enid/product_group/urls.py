from django.urls import path
from rest_framework.routers import DefaultRouter
from product_group import views

router = DefaultRouter()
router.register(r'product_group', views.ProductGroupViewSet, basename='product_group')

urlpatterns = [
    path('<int:pk>/products/', views.ProductGroupViewSet.as_view({'get': 'get_products'}), name="product_group_get_products"),
]


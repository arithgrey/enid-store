from django.contrib import admin
from django.views.static import serve
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
       title="API Store",
       default_version='v1',
       description="Enid Service store",
       contact=openapi.Contact(email="jmedrano9006@gmail.com"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', include('categories.urls')),    
    path('direccion/', include('address.urls')),    
    path('estado/', include('state.urls')),
    path('orden/', include('order.urls')),
    path('order/', include('order_oauth.urls')),
    path('order-search/', include('order_search.urls')),
    path('order-user/', include('order_user.urls')),
    path('order-payment-on-delivery/', include('order_payment_on_delivery.urls')),
    path('compra/', include('order_management.urls')),
    path('item-order/', include('item_order.urls')),
    path('product-category/', include('product_category_search.urls')),
    path('productos/', include('products.urls')),
    path('product-group/', include('product_group.urls')),        
    path('producto-variante/', include('product_variant.urls')),  
    path('variantes/', include('variants.urls')),        
    path('image/', include('image.urls')),
    path('user/', include('user.urls')),    
    path('search/', include('search.urls')),    
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('uploads/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('primary-components/', include('primary_components.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
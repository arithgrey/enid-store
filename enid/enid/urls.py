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
    path('api/categorias/', include('categories.urls')),    
    path('api/direccion/', include('address.urls')),    
    path('api/estado/', include('state.urls')),
    path('api/orden/', include('order.urls')),
    path('api/order/', include('order_oauth.urls')),
    path('api/order-search/', include('order_search.urls')),
    path('api/order-user/', include('order_user.urls')),
    path('api/compra/', include('order_management.urls')),
    path('api/lead-type/', include('lead_type.urls')),
    path('api/lead/', include('lead.urls')),
    path('api/lead-search/', include('lead_search.urls')),
    path('api/item-order/', include('item_order.urls')),
    path('api/product-category/', include('product_category_search.urls')),
    path('api/productos/', include('products.urls')),
    path('api/product-group/', include('product_group.urls')),        
    path('api/producto-variante/', include('product_variant.urls')),  
    path('api/variantes/', include('variants.urls')),        
    path('api/image/', include('image.urls')),
    path('api/user/', include('user.urls')),    
    path('api/search/', include('search.urls')),    
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('uploads/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
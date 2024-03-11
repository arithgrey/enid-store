from django.contrib import admin
from django.views.static import serve
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

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
    path('api/login/', include('login.urls')),
    path('api/', include('logout.urls')),
    path('api/item-order/', include('item_order.urls')),
    path('api/faq/', include('faqs.urls')),
    path('api/devoluciones/', include('returns.urls')),
    path('api/product-category/', include('product_category_search.urls')),
    path('api/productos/', include('products.urls')),
    path('api/product-group/', include('product_group.urls')),        
    path('api/producto-variante/', include('product_variant.urls')),  
    path('api/business/', include('business.urls')),
    path('api/variantes/', include('variants.urls')),        
    path('api/image/', include('image.urls')),
    path('', include('faqs.urls')),
    path('api/user/', include('user.urls')),    
    path('api/search/', include('search.urls')),    
    path('uploads/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
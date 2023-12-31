from django.contrib import admin
from django.views.static import serve
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/faq/', include('faqs.urls')),
    path('api/devoluciones/', include('returns.urls')),
    path('api/productos/', include('products.urls')),    
    path('api/producto-variante/', include('product_variant.urls')),    
    path('api/variantes/', include('variants.urls')),    
    path('api/cart/', include('cart.urls')),    
    path('api/item-cart/', include('item_cart.urls')),        
    path('api/image/', include('image.urls')),
    path('', include('faqs.urls')),
    path('uploads/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from rest_framework import generics
from rest_framework import viewsets
from product_variant.models import ProductVariant
from product_variant.serializers import ProductVariantSerializer, ProductVariantByProductSerializer


# Create your views here.
class ProducVariantVuewSet(viewsets.ModelViewSet):

    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer


class ProductVariantByProductView(generics.ListAPIView):
    serializer_class = ProductVariantByProductSerializer

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        return ProductVariant.objects.filter(product_id=product_id)

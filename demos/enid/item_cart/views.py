from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from item_cart.serializers import ItemCartSerializer
from item_cart.models import ItemCart
from products.models import Product
from item_cart.services.session_cart_service import CartService
from django.shortcuts import get_object_or_404

# Create your views here.
class ItemCartVuewSet(viewsets.ModelViewSet):
        
    queryset = ItemCart.objects.all()
    serializer_class = ItemCartSerializer
    cart_service = CartService()

    @action(detail=False, methods=['post'],url_path='add_to_cart')
    def add_to_cart(self,request):
        product_id=request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        quantity =  request.data.get('quantity',1)                
        user = request.user

        item_cart  = self.cart_service.add_to_cart(
            user=user, product=product, quantity=quantity, session=request.session)
            
        serializer = ItemCartSerializer(instance=item_cart)
   
        return Response(serializer.data, status=status.HTTP_201_CREATED)
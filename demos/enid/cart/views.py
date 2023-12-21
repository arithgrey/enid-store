from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from cart.models import Cart
from cart.serializers import CartSerializer
from cart.services.without_authentication import WithoutAuthentication
from item_cart.models import ItemCart
from item_cart.serializers import ItemCartSerializer

class CartVuewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(detail=False, methods=['GET'], url_path='productos')
    def products(self, request):
        if request.user.is_authenticated:
            user_cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            without_auth_service = WithoutAuthentication()
            user_cart = without_auth_service.get_or_create_cart(request.session)

        cart_items = ItemCart.objects.filter(cart=user_cart)
        serializer = ItemCartSerializer(cart_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from cart.models import Cart
from cart.serializers import CartSerializer
from item_cart.models import ItemCart
from item_cart.serializers import ItemCartSerializer
from django.shortcuts import get_object_or_404
from products.models import Product
from django.contrib.auth.decorators import login_required
import uuid


class CartVuewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(detail=False, methods=['get'], url_path='products')
    def get_cart_items(self, request):
        if request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(user=request.user)
        else:
            cart_id = request.session.get('cart_id')
            if not cart_id:
                return Response({"error": "No hay productos en el carrito"}, status=status.HTTP_404_NOT_FOUND)
            cart = get_object_or_404(Cart, unique_identifier=cart_id)
        
        cart_items = ItemCart.objects.filter(cart=cart)
        serializer = ItemCartSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['post'], url_path='add_to_cart')
    def add_to_cart(self, request):
        
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        
        # Obtener el carrito
        if request.user.is_authenticated:
            cart =  self.add_to_cart_authenticated(request, product_id)
        else:
            cart = self.add_to_cart_unauthenticated(request, product_id)
        
        serializer = CartSerializer(instance=cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @login_required
    def add_to_cart_authenticated(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = ItemCart.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
        return cart
    
    def add_to_cart_unauthenticated(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart_id = request.session.get('cart_id')
        
        # Si no hay un cart_id en la sesión, o si no existe un carrito con ese cart_id en la base de datos, creamos uno nuevo
        if not cart_id or not Cart.objects.filter(unique_identifier=cart_id).exists():
            unique_cart_identifier = str(uuid.uuid4())
            
            # Verificar si el unique_identifier ya existe en la base de datos
            while Cart.objects.filter(unique_identifier=unique_cart_identifier).exists():
                unique_cart_identifier = str(uuid.uuid4())
            
            cart = Cart.objects.create(unique_identifier=unique_cart_identifier)
            request.session['cart_id'] = unique_cart_identifier
            request.session.save()
        else:
            cart = get_object_or_404(Cart, unique_identifier=cart_id)
        
        # Aquí es donde comprobamos si el producto ya está en el carrito
        cart_item, created = ItemCart.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
        
        return cart_item
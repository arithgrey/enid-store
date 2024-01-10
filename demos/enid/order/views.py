from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from rest_framework.decorators import action
from order.serializer import OrderSerializer
from order.models import Order
from address.models import Address
from products.models import Product
from item_order.models import ItemOrder
from django.contrib.auth.models import User
from state.models import State
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=['post'], url_path='compra')
    def create_order(self, request):        
        data = request.data           
        serializer = OrderSerializer(data=data)
        if not serializer.is_valid():
            #print(serializer.errors) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:

            user = self.register_user(data["user"])
            address = self.register_address(data["address"], user)

            with transaction.atomic():
                order = self.create_order_instance(address)
                self.register_items_order(order, data["products"])
                serializer = OrderSerializer(order, context={'request': request})
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as e:  # Captura errores de validación
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def create_order_instance(self, address):
        return Order.objects.create(shipping_address=address)

    def register_items_order(self, order, products):
        for product in products:
            item = get_object_or_404(Product, id=product['id'], price=product['price'])
            ItemOrder.objects.create(
                order=order,
                product=item,
                quantity=product['quantity'],
                price=product["price"]
            )

    def register_user(self, user_data):
        
        user_data = {
            "email": user_data['email'],
            "defaults": {
                'username': user_data['email'],
                'first_name': user_data.get('name', '').split()[0],
                'last_name': ' '.join(user_data.get('name', '').split()[1:])
            }
        }
        user, _ = User.objects.get_or_create(**user_data)
               
        return user

    def register_address(self, address_data, user):
        
        address_data['state'] = State.objects.get(id=address_data["state"])
        address_data['user'] = user
        return Address.objects.create(**address_data)

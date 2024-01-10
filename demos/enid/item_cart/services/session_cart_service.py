from cart.models import Cart
from item_cart.models import ItemCart

class CartService:
        
    def add_to_cart(self, user, product, quantity, request):
        user_cart = self.get_or_create_cart(user, request)
        return self.add_item_on_cart(cart=user_cart, product=product, quantity=quantity)
        
    def add_item_on_cart(self, cart, product, quantity):
        if not cart:
            raise ValueError("No se pudo obtener o crear un carrito.")
        
        item, _ = ItemCart.objects.get_or_create(cart=cart, product=product)
        item.quantity += quantity
        item.save()
        return item

    def get_or_create_cart(self, user, request):
        if user and user.is_authenticated:
            try:                
                return Cart.objects.get(user=user)
            except Cart.DoesNotExist:
                pass
        
        cart_id = request.session.get('cart_id')
        print(cart_id)
        if cart_id:
            try:
                return Cart.objects.get(id=cart_id)
            except Cart.DoesNotExist:
                pass

        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
        return cart

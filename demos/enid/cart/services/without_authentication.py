from cart.models import Cart
class WithoutAuthentication:  
    
    def get_or_create_cart(self, session):        
        if 'cart_id' not in session:
            cart = Cart.objects.create()
            session['cart_id'] = cart.id
        return Cart.objects.get(id=session['cart_id'])
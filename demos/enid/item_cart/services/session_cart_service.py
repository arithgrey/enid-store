from cart.models import Cart
from item_cart.models import ItemCart
from cart.services.without_authentication import WithoutAuthentication

class CartService:
        
    def add_to_cart(self, user, product, quantity, session):

        if user and user.is_authenticated:            
            user_cart, created = Cart.objects.get_or_create(user=user)
        else:
            without_auth_service = WithoutAuthentication()
            user_cart = without_auth_service.get_or_create_cart(session)
                        
        return self.add_item_on_cart(cart=user_cart,product=product,quantity=quantity)
        
        
    def add_item_on_cart(self, cart, product, quantity):
        if not cart:            
            raise ValueError("No se pudo obtener o crear un carrito.")
        
        item, item_created = ItemCart.objects.get_or_create(cart=cart, product=product)
                
        if item_created:           
            item.quantity = quantity            
        else:            
            item.quantity += quantity
            
        item.save()
        return item

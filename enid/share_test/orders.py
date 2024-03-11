from order.models import Order
import random
from item_order.models import ItemOrder
from share_test.commons import CommonsTest

class OrderCreationHelper(CommonsTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)            
        
    
    def create_fake_order_with_products(self, user=None, store=None, num_products=3, **kwargs):
        
        if user is None:
            user = self.crear_fake_user()

        if store is None:
            store = self.create_fake_store()

        address = self.create_fake_address()

        if 'store' not in kwargs:
            kwargs['store'] = store

        order = Order.objects.create(user=user, shipping_address=address, **kwargs)
        products = [self.create_fake_product(store=store) for _ in range(num_products)]
    
        for product in products:
            quantity = random.randint(1, 10)
            price = product.price
            ItemOrder.objects.create(order=order, product=product, quantity=quantity, price=price)

        return order
    


class OrderCreationServiceHelper(OrderCreationHelper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)            

    def create_n_fake_orders(self, user=None, store=None, total_orders = 1, num_products=3, **kwargs):
                
        return [self.create_fake_order_with_products(
            user=user, store=store, num_products=num_products, **kwargs) 
            for _ in range(total_orders)]
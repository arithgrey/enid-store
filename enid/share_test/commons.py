from faker import Faker
from products.models import Product
from categories.models import Category
from store.models import Store

class CommonsTest:

    
    def create_fake_category(self, store = None):

        fake = Faker('es_MX')
        if not isinstance(store, Store):
            store = Store.objects.create(name=fake.company())

        return Category.objects.create(name=fake.word(), store=store)


    def create_fake_product(self, **kwargs):
        fake = Faker('es_MX')        

        defaults = {
            'name': fake.word(),
            'price': fake.random_int(min=100, max=10000)
        }
        
        params = {**defaults, **kwargs}

        if 'category' not in params:
            store = Store.objects.create(name=fake.company())
            params['store'] = store
            params['category'] = self.create_fake_category(store)

        product = Product.objects.create(**params)
        
        return product
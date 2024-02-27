from faker import Faker
from products.models import Product
from categories.models import Category
from store.models import Store
from lead.models import Lead
from lead_type.models import LeadType

class CommonsTest:

    def __init__(self):
        self.fake = Faker('es_MX')

    def create_fake_lead(self, **kwargs):
        store = self.create_fake_store()
        
        defaults = {
            "email": self.fake.email(), 
            "name": self.fake.name(),
            "phone_number": self.fake.phone_number().split('x')[0].strip(),
            "lead_type": LeadType.objects.create(name="En intento de compra"),
            "store":store
        }

        params = {**defaults, **kwargs}       
        return Lead.objects.create(**params)
        

    def create_fake_category(self, store = None):


        if not isinstance(store, Store):
            store = Store.objects.create(name=self.fake.company())

        return Category.objects.create(name=self.fake.word(), store=store)


    def create_fake_product(self, **kwargs):
        

        defaults = {
            'name': self.fake.word(),
            'price': self.fake.random_int(min=100, max=10000)
        }
        
        params = {**defaults, **kwargs}

        if 'category' not in params:
            store = Store.objects.create(name=self.fake.company())
            params['store'] = store
            params['category'] = self.create_fake_category(store)

        product = Product.objects.create(**params)
        
        return product
    
    def create_fake_store(self, **kwargs):
        
        defaults = {
            'name': self.fake.word(),            
        }
        
        params = {**defaults, **kwargs}
        store = Store.objects.create(**params)
        
        return store
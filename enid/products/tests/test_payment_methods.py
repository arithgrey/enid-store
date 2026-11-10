from django.test import TestCase
from products.models import Product, PaymentMethod
from categories.models import Category


class PaymentMethodModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.all().delete()
        Product.objects.all().delete()
        PaymentMethod.objects.all().delete()

    def setUp(self):
        self.category = Category.objects.create(name='Test Category', slug='test-cat-pm')
        self.stripe = PaymentMethod.objects.create(slug='stripe', name='Revisar y Pagar')
        self.contra = PaymentMethod.objects.create(slug='contra_entrega', name='Paga al recibir')
        PaymentMethod.objects.create(slug='express', name='Compra Express')

    def tearDown(self):
        Category.objects.all().delete()
        Product.objects.all().delete()
        PaymentMethod.objects.all().delete()

    def test_payment_method_model_exists(self):
        pm = PaymentMethod.objects.get(slug='stripe')
        self.assertEqual(pm.slug, 'stripe')
        self.assertEqual(str(pm), 'Revisar y Pagar')

    def test_product_has_payment_methods_m2m(self):
        product = Product.objects.create(
            name='Test PM M2M', specific_name='Test', price=100,
            category=self.category
        )
        product.payment_methods.add(self.stripe)
        self.assertIn('stripe', product.payment_methods.values_list('slug', flat=True))

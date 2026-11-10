from django.test import TestCase
from rest_framework.test import APIClient
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


class PaymentMethodAPITest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.all().delete()
        Product.objects.all().delete()
        PaymentMethod.objects.all().delete()

    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name='API Test Category', slug='api-test-cat-pm')
        self.stripe = PaymentMethod.objects.create(slug='stripe', name='Revisar y Pagar')
        self.contra = PaymentMethod.objects.create(slug='contra_entrega', name='Paga al recibir')
        self.express = PaymentMethod.objects.create(slug='express', name='Compra Express')

    def tearDown(self):
        Category.objects.all().delete()
        Product.objects.all().delete()
        PaymentMethod.objects.all().delete()

    def test_product_serializer_includes_payment_methods_slugs(self):
        product = Product.objects.create(
            name='Test API PM', specific_name='Test', price=100,
            category=self.category
        )
        product.payment_methods.set([self.stripe, self.contra])
        response = self.client.get(f'/productos/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('stripe', response.data['payment_methods'])
        self.assertIn('contra_entrega', response.data['payment_methods'])
        self.assertNotIn('express', response.data['payment_methods'])

    def test_payment_methods_list_endpoint(self):
        response = self.client.get('/payment-methods/')
        self.assertEqual(response.status_code, 200)
        slugs = [m['slug'] for m in response.data]
        self.assertIn('stripe', slugs)
        self.assertIn('contra_entrega', slugs)
        self.assertIn('express', slugs)

    def test_patch_product_updates_payment_methods(self):
        product = Product.objects.create(
            name='Test Patch PM', specific_name='Test', price=100,
            category=self.category
        )
        product.payment_methods.set([self.stripe, self.contra, self.express])
        response = self.client.patch(
            f'/productos/{product.id}/',
            data={'payment_methods': ['stripe']},
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.data['payment_methods']), ['stripe'])
        product.refresh_from_db()
        self.assertEqual(product.payment_methods.count(), 1)
        self.assertEqual(product.payment_methods.first().slug, 'stripe')

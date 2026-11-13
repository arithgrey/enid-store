from django.test import TestCase
from categories.models import Category
from products.models import Product


def _make_product():
    # El entorno siembra productos/categorías con ids explícitos vía post_migrate,
    # lo que deja la secuencia de Postgres desalineada. Reusamos una fila existente
    # (mismo patrón que revenue/tests/test_monthly.py) para evitar colisiones de pk.
    product = Product.objects.first()
    if product is not None:
        return product
    cat, _ = Category.objects.get_or_create(name='Cat cert', slug='cat-cert')
    return Product.objects.create(
        category=cat, name='Prod cert', specific_name='Prod cert', price=100, cost=50
    )


class ProductCertificationModelTest(TestCase):
    def test_default_certification_is_published(self):
        product = _make_product()
        self.assertEqual(product.certification, 'published')
        self.assertIsNone(product.certified_at)

    def test_certification_choices_are_three(self):
        keys = [c[0] for c in Product.CERTIFICATION_CHOICES]
        self.assertEqual(keys, ['published', 'candidate', 'certified'])

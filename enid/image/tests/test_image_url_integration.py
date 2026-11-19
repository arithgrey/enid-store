from django.conf import settings
from django.test import TestCase, override_settings

from image.models import Image
from image.serializers import ImageSerializer


class ImageUrlRelativeIntegrationTest(TestCase):
    """
    Por qué: la API debe devolver rutas relativas (/uploads/X) para que el
    navegador las resuelva contra el origen desde el que cargó la página
    (IP, dominio o localhost). Un host fijo en la URL rompe las imágenes
    fuera de ese host.

    Sin mocks: usa Postgres real del compose.
    """

    def setUp(self):
        self.image = Image.objects.create(title="seed-image", image="seed-image.png")

    @override_settings(DOMAIN="http://dominio-fijo.example:8000")
    def test_get_image_url_devuelve_ruta_relativa_aunque_domain_este_definido(self):
        persisted = Image.objects.get(pk=self.image.pk)

        self.assertEqual(persisted.get_image_url(), f"{settings.MEDIA_URL}seed-image.png")

    @override_settings(DOMAIN="")
    def test_get_image_url_devuelve_ruta_relativa_sin_domain(self):
        persisted = Image.objects.get(pk=self.image.pk)

        self.assertEqual(persisted.get_image_url(), f"{settings.MEDIA_URL}seed-image.png")

    @override_settings(DOMAIN="http://dominio-fijo.example:8000")
    def test_serializer_expone_get_image_url_relativo(self):
        data = ImageSerializer(Image.objects.get(pk=self.image.pk)).data

        self.assertEqual(data["get_image_url"], f"{settings.MEDIA_URL}seed-image.png")
        self.assertNotIn("dominio-fijo.example", data["get_image_url"])

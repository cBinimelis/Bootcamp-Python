from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

from .models import Laboratorio


# Create your tests here.
class LaboratorioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Labo 1", ciudad="Tangamandapio", pais="Maravillas"
        )

    def test_model_content(self):
        self.assertEqual(self.laboratorio.nombre, "Labo 1")
        self.assertEqual(self.laboratorio.ciudad, "Tangamandapio")
        self.assertEqual(self.laboratorio.pais, "Maravillas")

    def test_url_exists(self):
        response = self.client.get("/laboratorio/laboratorio/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("laboratorio:laboratorio_list"))
        self.assertEqual(response.status_code, 200)

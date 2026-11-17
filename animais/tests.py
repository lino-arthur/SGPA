
from datetime import date

from django.test import TestCase

from .models import Animal


class AnimalModelTest(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome="Rex",
            especie=Animal.Especie.CAO,
            sexo=Animal.Sexo.MACHO,
            idade_aproximada=3,
            data_resgate=date(2026, 11, 10),
            status=Animal.Status.RESGATADO,
        )

    def test_animal_e_cadastrado(self):
        self.assertEqual(Animal.objects.count(), 1)

    def test_nome_animal(self):
        self.assertEqual(self.animal.nome, "Rex")

    def test_especie_animal(self):
        self.assertEqual(
            self.animal.get_especie_display(),
            "Cão"
        )

    def test_status_inicial(self):
        self.assertEqual(
            self.animal.status,
            Animal.Status.RESGATADO
        )

    def test_representacao_textual(self):
        self.assertEqual(str(self.animal), "Rex")


from datetime import date

from django.test import TestCase

from animais.models import Animal
from .models import Adocao


class AdocaoModelTest(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome="Rex",
            especie=Animal.Especie.CAO,
            sexo=Animal.Sexo.MACHO,
            idade_aproximada=3,
            data_resgate=date(2026, 11, 10),
        )

        self.adocao = Adocao.objects.create(
            animal=self.animal,
            nome_interessado="João Silva",
            telefone="21999999999",
            email="joao@example.com",
            status=Adocao.Status.EM_ANALISE,
        )

    def test_adocao_cadastrada(self):
        self.assertEqual(Adocao.objects.count(), 1)

    def test_adocao_vinculada_ao_animal(self):
        self.assertEqual(self.adocao.animal, self.animal)

    def test_status_inicial(self):
        self.assertEqual(
            self.adocao.status,
            Adocao.Status.EM_ANALISE
        )

    def test_alteracao_de_status(self):
        self.adocao.status = Adocao.Status.APROVADO
        self.adocao.save()

        self.adocao.refresh_from_db()

        self.assertEqual(
            self.adocao.status,
            Adocao.Status.APROVADO
        )

    def test_animal_acessa_suas_adocoes(self):
        self.assertEqual(self.animal.adocoes.count(), 1)

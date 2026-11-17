
from datetime import date

from django.test import TestCase

from animais.models import Animal
from .models import HistoricoVeterinario


class HistoricoVeterinarioTest(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome="Rex",
            especie=Animal.Especie.CAO,
            sexo=Animal.Sexo.MACHO,
            idade_aproximada=3,
            data_resgate=date(2026, 11, 10),
        )

        self.historico = HistoricoVeterinario.objects.create(
            animal=self.animal,
            tipo_procedimento=HistoricoVeterinario.TipoProcedimento.VACINA,
            data_procedimento=date(2026, 11, 12),
            descricao="Aplicação de vacina antirrábica",
            observacoes="Procedimento realizado com sucesso",
        )

    def test_historico_cadastrado(self):
        self.assertEqual(
            HistoricoVeterinario.objects.count(), 1
        )

    def test_historico_vinculado_ao_animal(self):
        self.assertEqual(self.historico.animal, self.animal)

    def test_tipo_procedimento(self):
        self.assertEqual(
            self.historico.get_tipo_procedimento_display(),
            "Vacinação"
        )

    def test_animal_acessa_seu_historico(self):
        self.assertEqual(
            self.animal.historicos_veterinarios.count(), 1
        )

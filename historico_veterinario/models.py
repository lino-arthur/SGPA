
from django.db import models


class HistoricoVeterinario(models.Model):

    class TipoProcedimento(models.TextChoices):
        CONSULTA = "CONSULTA", "Consulta"
        VACINA = "VACINA", "Vacinação"
        TRATAMENTO = "TRATAMENTO", "Tratamento"
        EXAME = "EXAME", "Exame"
        OUTRO = "OUTRO", "Outro"

    animal = models.ForeignKey(
        "animais.Animal",
        on_delete=models.CASCADE,
        related_name="historicos_veterinarios"
    )

    tipo_procedimento = models.CharField(
        max_length=15,
        choices=TipoProcedimento.choices
    )

    data_procedimento = models.DateField()

    descricao = models.TextField()

    observacoes = models.TextField(
        blank=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.animal.nome} - {self.get_tipo_procedimento_display()}"

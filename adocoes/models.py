
from django.db import models


class Adocao(models.Model):

    class Status(models.TextChoices):
        EM_ANALISE = "EM_ANALISE", "Em análise"
        APROVADO = "APROVADO", "Aprovado"
        RECUSADO = "RECUSADO", "Recusado"
        CONCLUIDO = "CONCLUIDO", "Concluído"

    animal = models.ForeignKey(
        "animais.Animal",
        on_delete=models.PROTECT,
        related_name="adocoes"
    )

    nome_interessado = models.CharField(
        max_length=150
    )

    telefone = models.CharField(
        max_length=20
    )

    email = models.EmailField(
        blank=True
    )

    data_solicitacao = models.DateField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.EM_ANALISE
    )

    observacoes = models.TextField(
        blank=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.nome_interessado} - {self.animal.nome}"

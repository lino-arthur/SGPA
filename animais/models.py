
from django.db import models


class Animal(models.Model):

    class Especie(models.TextChoices):
        CAO = "CAO", "Cão"
        GATO = "GATO", "Gato"
        OUTRO = "OUTRO", "Outro"

    class Sexo(models.TextChoices):
        MACHO = "M", "Macho"
        FEMEA = "F", "Fêmea"
        NAO_INFORMADO = "N", "Não informado"

    class Status(models.TextChoices):
        RESGATADO = "RESGATADO", "Resgatado"
        TRATAMENTO = "TRATAMENTO", "Em tratamento"
        DISPONIVEL = "DISPONIVEL", "Disponível para adoção"
        ADOTADO = "ADOTADO", "Adotado"

    nome = models.CharField(max_length=100)
    especie = models.CharField(
        max_length=10,
        choices=Especie.choices
    )
    sexo = models.CharField(
        max_length=1,
        choices=Sexo.choices
    )
    idade_aproximada = models.PositiveSmallIntegerField()
    data_resgate = models.DateField()
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.RESGATADO
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

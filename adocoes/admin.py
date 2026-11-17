
from django.contrib import admin
from .models import Adocao


@admin.register(Adocao)
class AdocaoAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nome_interessado",
        "animal",
        "telefone",
        "data_solicitacao",
        "status",
    )

    list_filter = (
        "status",
        "data_solicitacao",
    )

    search_fields = (
        "nome_interessado",
        "animal__nome",
        "telefone",
    )

    ordering = ("-data_solicitacao",)

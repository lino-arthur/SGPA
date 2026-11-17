
from django.contrib import admin
from .models import HistoricoVeterinario


@admin.register(HistoricoVeterinario)
class HistoricoVeterinarioAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "animal",
        "tipo_procedimento",
        "data_procedimento",
    )

    list_filter = (
        "tipo_procedimento",
        "data_procedimento",
    )

    search_fields = (
        "animal__nome",
        "descricao",
    )

    ordering = ("-data_procedimento",)

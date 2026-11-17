
from django.contrib import admin
from .models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "especie",
        "sexo",
        "idade_aproximada",
        "data_resgate",
        "status",
    )

    list_filter = ("especie", "sexo", "status")
    search_fields = ("nome",)
    ordering = ("nome",)

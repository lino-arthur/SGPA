
from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal

        fields = [
            "nome",
            "especie",
            "sexo",
            "idade_aproximada",
            "data_resgate",
            "status",
        ]

        labels = {
            "nome": "Nome do animal",
            "especie": "Espécie",
            "sexo": "Sexo",
            "idade_aproximada": "Idade aproximada",
            "data_resgate": "Data do resgate",
            "status": "Status atual",
        }

        widgets = {
            "nome": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Digite o nome do animal",
            }),
            "especie": forms.Select(attrs={
                "class": "form-select",
            }),
            "sexo": forms.Select(attrs={
                "class": "form-select",
            }),
            "idade_aproximada": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0",
            }),
            "data_resgate": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),
            "status": forms.Select(attrs={
                "class": "form-select",
            }),
        }


from django import forms
from .models import Adocao


class AdocaoForm(forms.ModelForm):

    class Meta:
        model = Adocao

        fields = [
            "animal",
            "nome_interessado",
            "telefone",
            "email",
            "status",
            "observacoes",
        ]

        labels = {
            "animal": "Animal",
            "nome_interessado": "Nome do interessado",
            "telefone": "Telefone",
            "email": "E-mail",
            "status": "Status da adoção",
            "observacoes": "Observações",
        }

        widgets = {
            "animal": forms.Select(attrs={
                "class": "form-select"
            }),

            "nome_interessado": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nome completo do interessado"
            }),

            "telefone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "(00) 00000-0000"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "email@exemplo.com"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

            "observacoes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Observações adicionais (opcional)"
            }),
        }

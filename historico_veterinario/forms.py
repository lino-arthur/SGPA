
from django import forms
from .models import HistoricoVeterinario


class HistoricoVeterinarioForm(forms.ModelForm):

    class Meta:
        model = HistoricoVeterinario

        fields = [
            "animal",
            "tipo_procedimento",
            "data_procedimento",
            "descricao",
            "observacoes",
        ]

        labels = {
            "animal": "Animal",
            "tipo_procedimento": "Tipo de procedimento",
            "data_procedimento": "Data do procedimento",
            "descricao": "Descrição",
            "observacoes": "Observações",
        }

        widgets = {
            "animal": forms.Select(attrs={
                "class": "form-select"
            }),
            "tipo_procedimento": forms.Select(attrs={
                "class": "form-select"
            }),
            "data_procedimento": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
            "descricao": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Descreva o procedimento realizado"
            }),
            "observacoes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Observações adicionais (opcional)"
            }),
        }

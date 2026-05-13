from django import forms

from .models import Falta


class FaltaForm(forms.ModelForm):
    class Meta:
        model = Falta
        fields = ['aluno', 'disciplina', 'data', 'justificada']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

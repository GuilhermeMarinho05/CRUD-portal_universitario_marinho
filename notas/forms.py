from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):

    class Meta:
        model = Nota
        fields = ['aluno', 'disciplina', 'nota1', 'nota2']

    def clean(self):
        cleaned_data = super().clean()

        nota1 = cleaned_data.get("nota1")
        nota2 = cleaned_data.get("nota2")

        for nota in [nota1, nota2]:
            if nota is not None and (nota < 0 or nota > 10):
                raise forms.ValidationError("Notas devem estar entre 0 e 10.")

        return cleaned_data
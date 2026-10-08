from django import forms

from .models import Comentario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'texto']
        labels = {'nombre': 'Nombre', 'texto': 'Comentario'}
        widgets = {
            'nombre': forms.TextInput(attrs={'autocomplete': 'name', 'maxlength': 100}),
            'texto': forms.Textarea(attrs={'rows': 4, 'maxlength': 2000}),
        }

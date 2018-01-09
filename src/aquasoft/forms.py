from django import forms
from datetime import date
from .models import Curso

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nombre_curso" , "descripcion"]


class RegForm(forms.Form):
    nombre_curso = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)



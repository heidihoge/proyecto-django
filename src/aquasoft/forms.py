from django import forms
from datetime import date

class RegForm(forms.Form):
    nombre_curso = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)



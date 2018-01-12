from django import forms

from .models import Curso

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nombre_curso" , "descripcion"]
    def clean_nombre_curso(self):
        curso = self.cleaned_data.get("nombre_curso")
        if not "natacion" in curso:
            raise forms.ValidationError("Por favor ingresa un curso que sea de Natacion")
        return curso
class RegForm(forms.Form):
    nombre_curso = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)



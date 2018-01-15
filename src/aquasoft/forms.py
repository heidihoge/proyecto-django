from django import forms

from .models import Curso

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nombre_curso" , "descripcion"]
    def clean_nombre_curso(self):
        curso = self.cleaned_data.get("nombre_curso")
        if not "curso" in curso:
            raise forms.ValidationError("Por favor ingresa un curso que sea de Natacion")
        return curso

class ContactForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)



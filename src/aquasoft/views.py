from django.shortcuts import render
from .forms import RegForm
from .models import Curso
# Create your views here.
def inicio(request):
    form = RegForm(request.POST or None)
    titulo = "Hola"
    if form.is_valid():
        form_data = form.cleaned_data
        nombre_cur= form_data.get("nombre_curso")
        desc_cur = form_data.get("descripcion")
        obj = Curso.objects.create(nombre_curso = nombre_cur, descripcion= desc_cur)
    context = {
        "titulo" : titulo,
        "form" : form
    }
    return render(request,"inicio.html",context)
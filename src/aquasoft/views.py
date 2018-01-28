from __future__ import unicode_literals
from django.shortcuts import render
from .forms import ContactForm ,RegModelForm
from .models import Curso

# Create your views here.
def inicio(request):
    form = RegModelForm(request.POST or None)
    titulo = "Hola"
    context = {
        "titulo": titulo,
        "form": form
    }
    if form.is_valid():
        instance = form.save(commit=False) #esto es para que no se guarde hasta que cumpla lo que queramos
        #por ejemmplo, condicion de que si no se le carga una descripcion , por defecto coloque 'esto es un curso mas'
        if not instance.descripcion:
            instance.descripcion = "esto es un curso mas"
        instance.save() #esto es lo que hace que se guarde en la base de datos

        context = {
            "titulo": "Gracias por cargar un curso"

        }

        # form_data = form.cleaned_data
        # nombre_cur= form_data.get("nombre_curso")
        # desc_cur = form_data.get("descripcion")
        # obj = Curso.objects.create(nombre_curso = nombre_cur, descripcion= desc_cur)
    return render(request,"inicio.html",context)

def contact (request):
    titulo = "Hola"

    form = ContactForm (request.POST or None)
    context = {
        "form": form,
        "titulo": titulo,

    }
    if form.is_valid():
        print(form.cleaned_data)

        context = {
            "titulo": "Gracias por escribirnos"
        }
    return render(request, "forms.html", context)

def principal (request):
    return render(request, "base.html")
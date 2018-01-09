from django.contrib import admin
from .models import Curso
from .forms import RegModelForm

# Register your models here.
class AdminCurso(admin.ModelAdmin):
    list_display = ["__str__", "date","descripcion"]
    list_display_links = ["date" ]
    list_filter = ["nombre_curso"]
    list_editable = ["descripcion"]
    search_fields =  ["nombre_curso"]
    form = RegModelForm
    # class Meta:
    #     model = Curso

admin.site.register(Curso,AdminCurso)

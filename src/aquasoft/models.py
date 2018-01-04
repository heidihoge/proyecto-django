from django.db import models
import time
from datetime import date
# Create your models here.
class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100, blank=True,null=False)
    descripcion = models.CharField (max_length=100, blank=True,null=False)
    date = date.today()

    def __str__(self):
        return self.nombre_curso


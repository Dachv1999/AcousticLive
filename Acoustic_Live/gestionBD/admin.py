from django.contrib import admin
from .models import Leccion, Profesor, Estudiante, Cursa
# Register your models here.
admin.site.register(Leccion)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Cursa)
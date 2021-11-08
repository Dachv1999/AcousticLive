from django.contrib import admin
from .models import Cursa, Estudiante, Leccion, Profesor
# Register your models here.
admin.site.register(Leccion)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Cursa)
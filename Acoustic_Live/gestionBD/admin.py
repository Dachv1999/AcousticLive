from django.contrib import admin

# Register your models here.
from .models import Profesor
from .models import Leccion
admin.site.register(Profesor)
admin.site.register(Leccion)
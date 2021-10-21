from django.db import models
from django.db.models.fields import TextField
# Create your models here.
class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=50)
    email = models.EmailField()
    user_name = models.CharField(max_length=20)
    contrasenia = models.CharField(max_length=20)
    
class Leccion(models.Model):
    nombre_leccion = models.CharField(max_length=50)
    nivel =models.IntegerField()
    link = models.TextField()
    descripcion = models.TextField()
    numero_clase = models.IntegerField()
    idProfesor = models.ForeignKey(Profesor,on_delete=models.CASCADE)
    # def __str__(self):
    #     return "%s %s" % (self.nombre_leccion)

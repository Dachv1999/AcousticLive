from django.db import models
from django.db.models.fields import TextField
from django.db.models.deletion import CASCADE

# Create your models here.
class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=50)
    apellido_profesor = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    user_name = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)

class Leccion(models.Model):
    nombre_leccion = models.CharField(max_length=100)
    nivel =models.IntegerField()
    link = models.TextField()
    descripcion = models.TextField()
    idprofesor = models.ForeignKey(Profesor,on_delete=CASCADE)
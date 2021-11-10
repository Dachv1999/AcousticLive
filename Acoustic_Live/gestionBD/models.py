from django.db import models
from django.db.models.fields import TextField
from django.db.models.deletion import CASCADE

# Create your models here.
class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=50)
    apellido_profesor = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    user_name = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_profesor

class Leccion(models.Model):
    nombre_leccion = models.CharField(max_length=100)
    nivel =models.IntegerField()
    link = models.CharField(max_length=600)
    descripcion = models.TextField()
    idprofesor = models.ForeignKey(Profesor,on_delete=CASCADE)
    orden = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre_leccion

class Estudiante(models.Model):
    nombre_estudiante=models.CharField(max_length=100)
    apellidoP_estudiante=models.CharField(max_length=50)
    apellidoM_estudiante=models.CharField(max_length=50)
    usuario=models.CharField(max_length=50)
    correo_estudiante=models.CharField(max_length=100)
    contraseña_estudiante=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_estudiante

class Cursa(models.Model):
    visto = models.BooleanField()
    id_leccion= models.ForeignKey(Leccion,on_delete=CASCADE)
    id_profesor= models.ForeignKey(Profesor,on_delete=CASCADE, null=True)
    nivel_leccion = models.IntegerField(null=True)
    #id_estudiante =models.ForeignKey(Estudiante,on_delete=CASCADE)

    def __str__(self):
        return self.id_leccion
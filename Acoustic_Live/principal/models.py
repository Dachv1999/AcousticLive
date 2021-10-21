from django.db import models

# Create your models here.
class Profesor(models.Model):
    id =models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 20)
    email = models.EmailField(max_length=100)
    username =models.CharField(max_length=20)
   
class Leccion(models.Model):
    id =models.AutoField(primary_key=True)
    nombre =models.CharField(max_length=20)
    nivel = models.IntegerField()
    link = models.CharField(max_length=100)
    idProfesor = models.ForeignKey(Profesor,on_delete=models.CASCADE)
    numeroLeccion =models.IntegerField()
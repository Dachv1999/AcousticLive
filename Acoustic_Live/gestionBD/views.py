from django.shortcuts import render
from .models import Leccion, Profesor

# Create your views here.

def lista_principiante(request, id_profesor):
    lecciones = Leccion.objects.filter(nivel=1, idprofesor_id=id_profesor)
    profesores = Profesor.objects.filter(id=id_profesor)
    level = "Nivel Principiante"
    atras = "/Profesores_Nivel_Principiante/"
    contexto = {
        'profesores' : profesores,
        'lecciones' : lecciones,
        'nivel' : level,
        'atras' : atras

    }
    
    return render(request,'Vista_Universal_Lecciones.html', contexto)

def lista_medio(request, id_profesor):
    
    lecciones = Leccion.objects.filter(nivel=2, idprofesor_id=id_profesor)
    profesores = Profesor.objects.filter(id=id_profesor)
    level = "Nivel Medio"
    atras = "/Profesores_Nivel_Medio/"
    contexto = {
        'profesores' : profesores,
        'lecciones' : lecciones,
        'nivel' : level,
        'atras' : atras

    }
    
    return render(request,'Vista_Universal_Lecciones.html', contexto)

def lista_avanzado(request, id_profesor):
    lecciones = Leccion.objects.filter(nivel=3, idprofesor_id=id_profesor)
    profesores = Profesor.objects.filter(id=id_profesor)
    level = "Nivel Avanzado"
    atras = "/Profesores_Nivel_Avanzado/"
    contexto = {
        'profesores' : profesores,
        'lecciones' : lecciones,
        'nivel' : level,
        'atras' : atras

    }
    return render(request,'Vista_Universal_Lecciones.html', contexto)

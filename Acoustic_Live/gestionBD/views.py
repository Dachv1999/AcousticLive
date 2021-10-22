from django.shortcuts import render
from .models import Leccion, Profesor

# Create your views here.

def lista_principiante(request, id_profesor):
    lecciones = Leccion.objects.filter(nivel=1, idprofesor_id=id_profesor)
    profesores = Profesor.objects.filter(id=id_profesor)

    contexto = {
        'profesores' : profesores,
        'lecciones' : lecciones
    }
    
    return render(request,'Vista_Nivel_Principiante.html', contexto)

def lista_medio(request, id_profesor):
    
    lecciones = Leccion.objects.filter(nivel=2, idprofesor_id=id_profesor)
    profesores = Profesor.objects.filter(id=id_profesor)

    contexto = {
        'profesores' : profesores,
        'lecciones' : lecciones
    }
    
    return render(request,'Vista_Nivel_Medio.html', contexto)

def lista_avanzado(request, id_profesor):
    lecciones = Leccion.objects.filter(nivel=3, idprofesor_id=id_profesor)
    profesores = Profesor.objects.filter(id=id_profesor)

    contexto = {
        'profesores' : profesores,
        'lecciones' : lecciones
    }
    return render(request,'Vista_Nivel_Avanzado.html', contexto)

from django.shortcuts import render
from .models import Leccion, Profesor

# Create your views here.

def lista_principiante(request, id_profesor):
    lecciones = Leccion.objects.filter(nivel=1, idprofesor_id=id_profesor)
    profesores = Profesor.objects.filter(id=id_profesor)
    level = "Nivel Principiante"
    atras = "/Profesores_Nivel_Principiante/"
   
    cant = 0
    for leccion in lecciones:
        cant = cant + 1


    contexto = {
        'profesores' : profesores,
        'lecciones' : lecciones,
        'nivel' : level,
        'atras' : atras,
        'cantidad_videos' : cant
    }
    
    return render(request,'Vista_Universal_Lecciones.html', contexto)

def lista_medio(request, id_profesor):
    
    lecciones = Leccion.objects.filter(nivel=2, idprofesor_id=id_profesor)
    profesores = Profesor.objects.filter(id=id_profesor)
    level = "Nivel Medio"
    atras = "/Profesores_Nivel_Medio/"
    bandera = True
    contexto = {
        'profesores' : profesores,
        'lecciones' : lecciones,
        'nivel' : level,
        'atras' : atras,
        'bandera' : bandera

    }
    
    return render(request,'Vista_Universal_Lecciones.html', contexto)

def lista_avanzado(request, id_profesor):
    lecciones = Leccion.objects.filter(nivel=3, idprofesor_id=id_profesor)
    profesores = Profesor.objects.filter(id=id_profesor)
    level = "Nivel Avanzado"
    atras = "/Profesores_Nivel_Avanzado/"
    bandera = True;
    contexto = {
        'profesores' : profesores,
        'lecciones' : lecciones,
        'nivel' : level,
        'atras' : atras,
        'bandera' : bandera

    }
    return render(request,'Vista_Universal_Lecciones.html', contexto)



from django.shortcuts import render
from .models import Leccion, Profesor, Cursa

# Create your views here.

def lista_principiante(request, id_profesor):
    lecciones = Leccion.objects.filter(nivel=1, idprofesor_id=id_profesor).order_by('orden')
    profesores = Profesor.objects.filter(id=id_profesor)
    cursan = Cursa.objects.filter(id_profesor_id=id_profesor, nivel_leccion = 1)

    lista_vistos = []

    for cursa in cursan:
        lista_vistos.append(cursa.id_leccion_id)

    cant = 0
    for leccion in lecciones:
        cant = cant + 1

    cant_tiqueados = 0
    for cursa in cursan:
        cant_tiqueados = cant_tiqueados + 1
    
    if cant != 0:
        porcentaje_vistos = int((cant_tiqueados * 100) / cant)
    else:
        porcentaje_vistos = 0 


    level = "Nivel Principiante"
    atras = "/Profesores_Nivel_Principiante/"
    nivel = 1
    tamanio_barra_progreso = str(porcentaje_vistos) +'%'
    contexto = {
        'profesores' : profesores,
        'lecciones' : lecciones,
        'nivel' : level,
        'nivel_leccion' : nivel,
        'id_profesor' : id_profesor,
        'atras' : atras,
        'cantidad' : cant,
        'lista_vistos' : lista_vistos,
        'tiqueados' : cant_tiqueados,
        'tamanio_barra_progreso' : tamanio_barra_progreso
    }
    
    return render(request,'Vista_Universal_Lecciones.html', contexto)

def lista_medio(request, id_profesor):
    
    lecciones = Leccion.objects.filter(nivel=2, idprofesor_id=id_profesor).order_by('orden')
    profesores = Profesor.objects.filter(id=id_profesor)
    cursan = Cursa.objects.filter(id_profesor_id=id_profesor, nivel_leccion = 2)

    lista_vistos = []

    for cursa in cursan:
        lista_vistos.append(cursa.id_leccion_id)

    cant = 0
    for leccion in lecciones:
        cant = cant + 1

    cant_tiqueados = 0
    for cursa in cursan:
        cant_tiqueados = cant_tiqueados + 1

    if cant != 0:
        porcentaje_vistos = int((cant_tiqueados * 100) / cant)
    else:
        porcentaje_vistos = 0 

    level = "Nivel Medio"
    atras = "/Profesores_Nivel_Medio/"
    bandera = True
    nivel = 2
    tamanio_barra_progreso = str(porcentaje_vistos) +'%'
    contexto = {
        'profesores' : profesores,
        'lecciones' : lecciones,
        'nivel' : level,
        'nivel_leccion' : nivel,
        'id_profesor' : id_profesor,
        'atras' : atras,
        'bandera' : bandera,
        'cantidad' : cant,
        'lista_vistos' : lista_vistos,
        'tiqueados' : cant_tiqueados,
        'tamanio_barra_progreso' : tamanio_barra_progreso

    }
    
    return render(request,'Vista_Universal_Lecciones.html', contexto)

def lista_avanzado(request, id_profesor):
    lecciones = Leccion.objects.filter(nivel=3, idprofesor_id=id_profesor).order_by('orden')
    profesores = Profesor.objects.filter(id=id_profesor)
    cursan = Cursa.objects.filter(id_profesor_id=id_profesor, nivel_leccion = 3)

    lista_vistos = []

    for cursa in cursan:
        lista_vistos.append(cursa.id_leccion_id)

    cant = 0
    for leccion in lecciones:
        cant = cant + 1

    cant_tiqueados = 0
    for cursa in cursan:
        cant_tiqueados = cant_tiqueados + 1

    if cant != 0:
        porcentaje_vistos = int((cant_tiqueados * 100) / cant)
    else:
        porcentaje_vistos = 0 

    level = "Nivel Avanzado"
    atras = "/Profesores_Nivel_Avanzado/"
    bandera = True
    nivel = 3
    tamanio_barra_progreso = str(porcentaje_vistos) +'%'
    contexto = {
        'profesores' : profesores,
        'lecciones' : lecciones,
        'nivel' : level,
        'nivel_leccion' : nivel,
        'id_profesor' : id_profesor,
        'atras' : atras,
        'bandera' : bandera,
        'cantidad' : cant,
        'lista_vistos' : lista_vistos,
        'tiqueados' : cant_tiqueados,
        'tamanio_barra_progreso' : tamanio_barra_progreso

    }
    return render(request,'Vista_Universal_Lecciones.html', contexto)



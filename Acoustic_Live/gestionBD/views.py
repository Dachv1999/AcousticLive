from django.shortcuts import render, redirect
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


def crud_profesores(request, nivel): #CRUD Profesores

    lecciones = Leccion.objects.filter(nivel=nivel, idprofesor_id=3).order_by('orden')

    cant = 0
    for leccion in lecciones:
        cant = cant + 1
        
    contexto = {
        'lecciones' : lecciones,
        'cantidad' : cant,
        'nivel' : nivel,

    }
    return render(request,'CRUD_Profesores.html', contexto)

def mover_video_arriba(request, id_profesor, orden_video, num_nivel):
    lecciones1 = Leccion.objects.get(nivel= num_nivel, idprofesor_id=id_profesor, orden = orden_video)
    lecciones2 = Leccion.objects.get(nivel= num_nivel, idprofesor_id=id_profesor, orden = orden_video- 1)
    redireccion = '/Mis_Videos/'+ str(num_nivel) +'/'

    lecciones2.orden = lecciones2.orden + 1
    lecciones1.orden = lecciones1.orden - 1
    
    lecciones1.save()
    lecciones2.save()
    return redirect(redireccion)

def mover_video_abajo(request, id_profesor, orden_video, num_nivel):
    lecciones1 = Leccion.objects.get(nivel= num_nivel, idprofesor_id=id_profesor, orden = orden_video)
    lecciones2 = Leccion.objects.get(nivel= num_nivel, idprofesor_id=id_profesor, orden = orden_video+ 1)
    redireccion = '/Mis_Videos/'+ str(num_nivel) +'/'

    lecciones2.orden = lecciones2.orden - 1
    lecciones1.orden = lecciones1.orden + 1
    
    lecciones1.save()
    lecciones2.save()
    return redirect(redireccion)


def eliminar_video_profesor(request, id_profesor, leccion_id, orden_video, nivel_leccion):
 
    leccion_a_eliminar = Leccion.objects.get( id = leccion_id, idprofesor_id=id_profesor, nivel = nivel_leccion)
    leccion_a_eliminar.delete()

    lecciones = Leccion.objects.filter( idprofesor_id=id_profesor, nivel = nivel_leccion)
     
    orden_nuevo = 1
    for leccion in lecciones:
       
       leccion.orden = orden_nuevo
       orden_nuevo = orden_nuevo + 1
       leccion.save()

    redireccion = '/Mis_Videos/'+ str(nivel_leccion) +'/'  
    return redirect(redireccion)


    
def Vista_Universal_Para_Profesor(request, id_profesor, nivel):
    lecciones = Leccion.objects.filter(nivel=nivel, idprofesor_id=id_profesor).order_by('orden')
    profesores = Profesor.objects.filter(id=id_profesor)

    cant = 0
    for leccion in lecciones:
        cant = cant + 1
        
    level = " " 

    if nivel == 1:
        level = "Nivel Principiante"
    elif nivel == 2:
        level = "Nivel Medio"
    else:
        level = "Nivel Avanzado"

    atras = "/Mis_Videos/" + str(nivel)
    contexto = {
        'profesores' : profesores,
        'lecciones' : lecciones,
        'nivel_leccion' : level,
        'id_profesor' : id_profesor,
        'atras' : atras,
        'cantidad' : cant,
    }
    
    return render(request,'Vista_Universal_Lecciones_For_Profesor.html', contexto)
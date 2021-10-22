from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from gestionBD.models import Leccion, Profesor


def niveles(request): #Vista niveles
    doc_externo = open("Acoustic_Live/Templates/Division_Niveles.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)
    
    return HttpResponse(documento)


def nivel_medio(request): #Vista nivel medio
    doc_externo = open("Acoustic_Live/Templates/Vista_Nivel_Medio.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()
    documento = plt.render(ctx)
    
    return HttpResponse(documento)

def nivel_avanzado(request): #Vista nivel avanzado
    doc_externo = open("Acoustic_Live/Templates/Vista_Nivel_Avanzado.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()
    documento = plt.render(ctx)
    
    return HttpResponse(documento)

def formulario_nuevoVideo(request):
    doc_externo = open("Acoustic_Live/Templates/formulario.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()
    documento = plt.render(ctx)

    return HttpResponse(documento)

def profesoresNP(request): #Vista profesoresNP
    doc_externo = open("Acoustic_Live/Templates/Vista_Profesores_NP.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()
    documento = plt.render(ctx)
    
    return HttpResponse(documento)

def profesoresNM(request): #Vista profesoresNM
    doc_externo = open("Acoustic_Live/Templates/Vista_Profesores_NM.html")
    
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()
    documento = plt.render(ctx)
    
    return HttpResponse(documento)

def profesoresNA(request): #Vista profesoresNA
    doc_externo = open("Acoustic_Live/Templates/Vista_Profesores_NA.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()
    documento = plt.render(ctx)
    
    return HttpResponse(documento)

def envio_formulario(request):
    nombre=request.POST.get('nombre','')
    descripcion= request.POST.get('descripcion','')
    link= request.POST.get('link','')
  
    lecc=Leccion(nombre_leccion = nombre, nivel = 3 ,link=link, descripcion = descripcion, idprofesor_id =1 )
    lecc.save()

    return render (request, "prueba_envio_formulario.html",{"nombre":nombre, "descripcion": descripcion, "link":link} )
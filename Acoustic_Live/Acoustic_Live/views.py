from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render, redirect
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

def formulario_nuevoVideo(request):

    if request.method=="POST":
        nombre=request.POST.get('nombre','')
        descripcion= request.POST.get('descripcion','')
        link= request.POST.get('link','')
        niveles= request.POST.get('nivel','')

        lecciones = Leccion.objects.filter(nivel=niveles, idprofesor_id=1)

        if(len(nombre) > 50):
            return redirect("/formulario/?error_nombre_muy_grande")

        if(len(descripcion)>500):
            return redirect("/formulario/?error_descripcion_muy_grande")

        if(len(descripcion)<20 and len(descripcion)>0):
            return redirect("/formulario/?error_descripcion_muy_pequeña")

        if ((len(nombre)) != 0 and (len(descripcion)) != 0 and (len(link)) != 0 and (len(niveles)) != 0 ):
            hayVideo=False
            for leccion in lecciones:
                if hayVideo==False:
                    if leccion.link==link:
                        hayVideo=True
            if hayVideo==True:  
                return redirect("/formulario/?videoExiste")
            else:
                # lecc=Leccion(nombre_leccion = nombre, nivel=niveles,link=link, descripcion = descripcion, idprofesor_id =1 )
                # lecc.save()
                return redirect("/formulario/?VideoGuardado")
        else:
            return redirect("/formulario/?Alguno_Esta_Vacio")
            
    return render (request, "formulario.html")
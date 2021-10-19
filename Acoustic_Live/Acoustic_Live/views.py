from django.http import HttpResponse
from django.template import Template, Context


def niveles(request): #Vista niveles
    doc_externo = open("Acoustic_Live/Templates/Division_Niveles.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()
    documento = plt.render(ctx)
    
    return HttpResponse(documento)

def nivel_principiante(request): #Vista nivel principiante
    doc_externo = open("Acoustic_Live/Templates/Vista_Nivel_Principiante.html")
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
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

def hijo(request): #Vista nivel principiante
    doc_externo = open("Acoustic_Live/Templates/hijo.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()
    documento = plt.render(ctx)
    
    return HttpResponse(documento)
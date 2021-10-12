from django.http import HttpResponse
from django.template import Template, Context


def niveles(request): #Vista niveles
    doc_externo = open("Acoustic_Live/Templates/Vista_Niveles.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()
    documento = plt.render(ctx)
    
    return HttpResponse(documento)
from django.shortcuts import render
from .models import Leccion

# Create your views here.

def listar(request):

    lecciones = Leccion.objects.filter(nivel=1, idprofesor=1)

    contexto = {
        'lecciones' : lecciones
    }
    
    return render(request, 'Vista_Nivel_Principiante.html', contexto)
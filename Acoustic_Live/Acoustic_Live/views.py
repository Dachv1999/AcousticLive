from django.http import HttpResponse
from django.template import Template, Context, context
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

def profesoresNP(request): #Vista profesoresNivelPrincipante
    cursos_profesor1= Leccion.objects.filter(nivel=1, idprofesor_id=1)
    cantidad_cursos1 =cursos_profesor1.count()
    cursos_profesor2= Leccion.objects.filter(nivel=1, idprofesor_id=2)
    cantidad_cursos2 =cursos_profesor2.count()
    cursos_profesor3= Leccion.objects.filter(nivel=1, idprofesor_id=3)
    cantidad_cursos3 =cursos_profesor3.count()
    doc_externo = open("Acoustic_Live/Templates/Vista_Profesores_NP.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    
    ctx = Context({'cantidad_cursos_1':cantidad_cursos1,'cantidad_cursos_2':cantidad_cursos2,'cantidad_cursos_3':cantidad_cursos3})
    documento = plt.render(ctx)

    return HttpResponse(documento)

def profesoresNM(request): #Vista profesoresNM
    cursos_profesor1= Leccion.objects.filter(nivel=2, idprofesor_id=1)
    cantidad_cursos1 =cursos_profesor1.count()
    cursos_profesor2= Leccion.objects.filter(nivel=2, idprofesor_id=2)
    cantidad_cursos2 =cursos_profesor2.count()
    cursos_profesor3= Leccion.objects.filter(nivel=2, idprofesor_id=3)
    cantidad_cursos3 =cursos_profesor3.count()
    doc_externo = open("Acoustic_Live/Templates/Vista_Profesores_NM.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context({'cantidad_cursos_1':cantidad_cursos1,'cantidad_cursos_2':cantidad_cursos2,'cantidad_cursos_3':cantidad_cursos3})
    documento = plt.render(ctx)

    return HttpResponse(documento)

def profesoresNA(request): #Vista profesoresNA
    cursos_profesor1= Leccion.objects.filter(nivel=3, idprofesor_id=1)
    cantidad_cursos1 =cursos_profesor1.count()
    cursos_profesor2= Leccion.objects.filter(nivel=3, idprofesor_id=2)
    cantidad_cursos2 =cursos_profesor2.count()
    cursos_profesor3= Leccion.objects.filter(nivel=3, idprofesor_id=3)
    cantidad_cursos3 =cursos_profesor3.count()
    doc_externo = open("Acoustic_Live/Templates/Vista_Profesores_NA.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context({'cantidad_cursos_1':cantidad_cursos1,'cantidad_cursos_2':cantidad_cursos2,'cantidad_cursos_3':cantidad_cursos3})
    documento = plt.render(ctx)

    return HttpResponse(documento)

def formulario_nuevoVideo(request):

    if request.method=="POST":
        nombre=request.POST.get('nombre','')
        descripcion= request.POST.get('descripcion','')
        link= request.POST.get('link','')
        niveles= request.POST.get('nivel','')

        lecciones = Leccion.objects.filter(nivel=niveles, idprofesor_id=1)
        nombre1 = nombre.strip()
        descripcion1 = descripcion.strip()
        link1 = link.strip()

        auxiliar_descripcion =descripcion.upper()
        auxiliar_nombre = nombre.upper() 
        
        if ((len(nombre1)) != 0 and (len(descripcion1)) != 0 and (len(link1)) != 0):
            if(len(nombre)>50):
                return redirect("/formulario/?error_nombre_muy_grande")
            if(len(descripcion)>500):
                return redirect("/formulario/?error_descripcion_muy_grande")
            if(len(descripcion)<20 ):
                return redirect("/formulario/?error_descripcion_muy_pequeña")
            
            encontre = False
            numero =0
            n=''
            while(numero<len(auxiliar_nombre)-2 and not encontre):
                if auxiliar_nombre[numero]==auxiliar_nombre[numero+1] and auxiliar_nombre[numero]==auxiliar_nombre[numero+2] :
                    n =nombre[numero]
                    encontre = True
                numero += 1
            if(encontre):
                doc_externo=open("D:/universidadd/Ingenieria de Software/AcousticLive/Acoustic_Live/Acoustic_Live/Templates/formulario.html")
                plt = Template(doc_externo.read()) #documento almacenado
                doc_externo.close()
                ctx = Context({"letra_encontrada_nombre":n})
                documento =plt.render(ctx)
                return HttpResponse(documento)
            ###para la descripcion
            encontre1 = False
            contador1 =0
            n1=''
            while(contador1<len(auxiliar_descripcion)-2 and not encontre1):
                if auxiliar_descripcion[contador1]==auxiliar_descripcion[contador1+1] and auxiliar_descripcion[contador1]==auxiliar_descripcion[contador1+2] :
                    n1 =descripcion[contador1]
                    encontre1 = True
                contador1 += 1
            if(encontre1):
                doc_externo=open("D:/universidadd/Ingenieria de Software/AcousticLive/Acoustic_Live/Acoustic_Live/Templates/formulario.html")
                plt = Template(doc_externo.read()) #documento almacenado
                doc_externo.close()
                ctx = Context({"letra_encontrada_descripcion":n1})
                documento =plt.render(ctx)
                return HttpResponse(documento)
            ###fin
            if(not('https://www.youtube.com/' in link)):
                return redirect("/formulario/?error_verifique_link")
            hayVideo=False
            for leccion in lecciones:
                if hayVideo==False:
                    if leccion.link==link:
                        hayVideo=True
            if hayVideo==True:  
                return redirect("/formulario/?videoExiste")
            else:
                lecc=Leccion(nombre_leccion = nombre, nivel=niveles,link=link, descripcion = descripcion, idprofesor_id =1 )
                lecc.save()
                return redirect("/formulario/?VideoGuardado")
        else:
            return redirect("/formulario/?Alguno_Esta_Vacio")
            
    return render (request, "formulario.html")

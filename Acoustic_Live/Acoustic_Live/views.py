from django.http import HttpResponse
from django.template import Template, Context, context
from django.shortcuts import render, redirect
from gestionBD.models import Leccion, Profesor
from tkinter import messagebox as MessageBox
from django.contrib import messages


def niveles(request): #Vista niveles
    doc_externo = open("Acoustic_Live/Templates/Division_Niveles.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)
    
    return HttpResponse(documento)

def login(request): #Login
    doc_externo = open("Acoustic_Live/Templates/login.html")
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

        lecciones = Leccion.objects.filter(idprofesor_id=1)
        nombre1 = nombre.strip()
        descripcion1 = descripcion.strip()
        link1 = link.strip()

        auxiliar_descripcion =descripcion.upper()
        auxiliar_nombre = nombre.upper() 
        
        if ((len(nombre1)) != 0 and (len(descripcion1)) != 0 and (len(link1)) != 0):
            if(len(nombre)>50):
                messages.add_message(request=request, level=messages.WARNING, message = "El nombre es muy grande")
                return redirect("/formulario/")
            if(len(descripcion)>500):
                messages.add_message(request=request, level=messages.WARNING, message = "La descripción es muy grande")
                return redirect("/formulario/")
            if(len(descripcion)<20 ):
                messages.add_message(request=request, level=messages.WARNING, message = "La descripción es muy pequeña")
                return redirect("/formulario/")
            
            valido = True
            i = 0
            while(i<len(nombre) and valido):
                aux = (int)(ord(nombre[i]))
                letrita = nombre[i]
                if (not((aux>64 and aux<91) or (aux>96 and aux<123) or (aux>47 and aux<59) \
                    or (aux==40 or aux==41 or aux==32 or aux==46 or aux==44
                    or letrita=="¿" or aux==63 or aux==45 or letrita=='!' or aux==35
                    or aux==58 or letrita=="á" or letrita=="é" or letrita=="í"
                    or letrita=="ó" or letrita=="ú" or letrita=="Á" or letrita=="É"
                    or letrita=="Í" or letrita=="Ó" or letrita=="Ú"))):
                    
                    valido = False
                i +=1
                
            if valido== False:
                messages.add_message(request=request, level=messages.WARNING, message = "El nombre contiene carcteres inválidos")
                return redirect("/formulario/")        
            #letra repetida
            encontre = False
            numero =0
            n=''
            while(numero<len(auxiliar_nombre)-2 and not encontre):
                codigo = (ord(auxiliar_nombre[numero]))
                if not(codigo>47 and codigo<59):
                    if auxiliar_nombre[numero]==auxiliar_nombre[numero+1] and auxiliar_nombre[numero]==auxiliar_nombre[numero+2] :
                        n =nombre[numero]
                        encontre = True
                numero += 1
            if(encontre):
                doc_externo=open("Acoustic_Live/Templates/formulario.html")
                plt = Template(doc_externo.read()) #documento almacenado
                doc_externo.close()
                #ctx = Context({"letra_encontrada_nombre":n})
                #documento =plt.render(ctx)
                #return HttpResponse(documento)
                messages.add_message(request=request, level=messages.WARNING, message = "El carácter '" + n + "' no debería repetirse tantas veces en el nombre")
                return redirect("/formulario/") 
            ###para la descripcion
            encontre1 = False
            contador1 =0
            n1=''
            while(contador1<len(auxiliar_descripcion)-2 and not encontre1):
                codigoDescripcion = (ord(auxiliar_descripcion[contador1]))
                if not(codigoDescripcion>47 and codigoDescripcion<59):
                    if auxiliar_descripcion[contador1]==auxiliar_descripcion[contador1+1] and auxiliar_descripcion[contador1]==auxiliar_descripcion[contador1+2] :
                        n1 =descripcion[contador1]
                        encontre1 = True
                contador1 += 1
            if(encontre1):
                doc_externo=open("Acoustic_Live/Templates/formulario.html")
                plt = Template(doc_externo.read()) #documento almacenado
                doc_externo.close()
                #ctx = Context({"letra_encontrada_descripcion":n1})
                #documento =plt.render(ctx)
                #return HttpResponse(documento)
                messages.add_message(request=request, level=messages.WARNING, message = "El carácter '" + n1 + "' no debería repetirse tantas veces en la descripción")
                return redirect("/formulario/") 
            ###fin
            #verficar link 
            link_auxi1="https://www.youtube.com/embed/"

            if(not('https://youtu.be/' in link)):
                messages.add_message(request=request, level=messages.WARNING, message = "Verifique el link que ingresó")
                return redirect("/formulario/")
            else:
                link=link_auxi1+link[17:]
            hayVideo=False
            for leccion in lecciones:
                if hayVideo==False:
                    if leccion.link==link:
                        hayVideo=True
            if hayVideo==True:  
                messages.add_message(request=request, level=messages.ERROR, message = "El video que ingresó ya existe")
                return redirect("/formulario/")
            else:
                lecc=Leccion(nombre_leccion = nombre, nivel=niveles,link=link, descripcion = descripcion, idprofesor_id =1 )
                lecc.save()
                messages.add_message(request=request, level=messages.SUCCESS, message = "Video guardado correctamente")
                return redirect("/formulario/")
        else:
            messages.add_message(request=request, level=messages.ERROR, message = "Por favor revise los campos")
            return redirect("/formulario/")
    
    return render (request, "formulario.html")
        


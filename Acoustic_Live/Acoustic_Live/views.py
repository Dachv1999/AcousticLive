from django.http import HttpResponse
from django.template import Template, Context, context
from django.shortcuts import render, redirect
from gestionBD.models import Leccion, Profesor, Estudiante
from tkinter import messagebox as MessageBox
from django.contrib import messages

def inicio(request): #Vista Inicio
    doc_externo = open("Acoustic_Live/Templates/Inicio.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)
    
    return HttpResponse(documento)


def inicio_profesores(request): #Vista Inicio de profesores
    doc_externo = open("Acoustic_Live/Templates/Vista_Principal_Profesores.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)
    
    return HttpResponse(documento)    

def niveles(request): #Vista niveles
    doc_externo = open("Acoustic_Live/Templates/Division_Niveles.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)
    
    return HttpResponse(documento)

def login(request): 
    if request.method=="POST":
        usuario=request.POST.get('usuario','')
        contraseña=request.POST.get('contraseña','')
        if len(contraseña)==0 or len(usuario)==0:
            messages.add_message(request=request, level=messages.WARNING, message = "Porfavor llene todos los campos")
            return redirect("/Login/")
        elif validar(usuario)==False:
            messages.add_message(request=request, level=messages.WARNING, message = "Error el nombre de usuario no es valido")
            return redirect("/Login/")
    
    return render (request, "login.html")

def validar(nombreUsuario):
    valido_usuario = True
    i = 0
    while(i<len(nombreUsuario) and valido_usuario):
        aux = (int)(ord(nombreUsuario[i]))
        letrita = nombreUsuario[i]
        if (not((aux>64 and aux<91) or (aux>96 and aux<123)or (aux>47 and aux<59)
            or letrita=="á" or letrita=="é" or letrita=="í" or letrita=="_" or letrita=="-"
            or letrita=="ó" or letrita=="ú" or letrita=="Á" or letrita=="É"
            or letrita=="Í" or letrita=="Ó" or letrita=="Ú" or letrita==" ")):
                    
            valido_usuario = False
        i +=1
    return valido_usuario

def espacio(palabra):
    res=False
    contador=0
    aux=0
    control=0
    while(contador<2 and aux<len(palabra)and control<100):
        control=control+1
        if(palabra[aux]==" "):
            contador=contador+1
        aux=aux+1
    if(contador==2):
        res=True
    if(contador==1 and len(palabra)==1):
        res=True
    return res


def validarNombres(palabra):
    valido = True
    i = 0
    while(i<len(palabra) and valido):
        aux = (int)(ord(palabra[i]))
        letrita = palabra[i]
        if (not((aux>64 and aux<91) or (aux>96 and aux<123)
            or letrita=="á" or letrita=="é" or letrita=="í"
            or letrita=="ó" or letrita=="ú" or letrita=="Á" or letrita=="É"
            or letrita=="Í" or letrita=="Ó" or letrita=="Ú" or letrita==" ")):
                    
            valido = False
        i +=1
    return valido

def validarCorreo(correo):
    valido_correo = True
    i = 0
    while(i<len(correo) and valido_correo):
        aux = (int)(ord(correo[i]))
        letrita = correo[i]
        if (not((aux>64 and aux<91) or (aux>96 and aux<123)or (aux>47 and aux<59)
            or letrita=="á" or letrita=="é" or letrita=="í" or letrita=="_" or letrita=="-"
            or letrita=="ó" or letrita=="ú" or letrita=="Á" or letrita=="É"
            or letrita=="Í" or letrita=="Ó" or letrita=="Ú" or letrita=="@"
            or letrita==".")):
            valido_correo = False
        i +=1
    return valido_correo

def mensaje(req,mensajeError):  
    messages.add_message(request=req, level=messages.WARNING, message = mensajeError)

def validarTamaño(palabra,maximo,minimo):
    
    cadena=-1
    if(len(palabra)>maximo):
        cadena=1
        
    else:
        if(len(palabra)<minimo):
            cadena=2
    return cadena

def generador(variable,numero):
    
    cadena=False
    if(numero==1):
        cadena="Error el campo "+variable+" es muy grande"
        
    else:
        if(numero==2):
            cadena="Error el campo "+variable+" es muy pequeño"
    return cadena
def Formulario_Registro(request):
    if request.method=="POST":
        nombre=request.POST.get('nombre','')
        apellidoPaterno=request.POST.get('apellido_paterno', '')
        apellidoMaterno=request.POST.get('apellido_materno','')
        nombreUsuario=request.POST.get('nombreUsuario','')
        correo= request.POST.get('correo','')
        contraseña= request.POST.get('contraseña','')
        confirmacion= request.POST.get('confirmacion','')
        res=redirect("/Formulario_Registro/")

        if(len(nombre)!=0 and len(correo)!=0 and len(contraseña)!=0 and len(nombreUsuario)!=0 and len(confirmacion)!=0):
            
            
            validoNombre=validarNombres(nombre)
            validoApePat=validarNombres(apellidoPaterno)
            validoApeMat=validarNombres(apellidoMaterno)
            valido_usuario = validar(nombreUsuario)
            valido_correo=validarCorreo(correo)

            if((len(apellidoPaterno)==0 and len(apellidoMaterno)==0)):
                mensaje(request,"Error debe ingresar al menos un apellido")
                return res
            if(validoNombre==False):
                mensaje(request,"Nombre ingresado invalido")
                return res
            if(validoApePat==False):
                mensaje(request,"Apellido paterno ingresado invalido")
                return res
            if(validoApeMat==False):
                mensaje(request,"Apellido materno ingresado invalido")
                return res

            if(valido_usuario==False):
                mensaje(request,"Nombre de usuario invalido")
                return res
        
            if(espacio(nombre)):
                mensaje(request,"Error el nombre debe tener caracteres alfabéticos")
                return res
            if(espacio(apellidoPaterno)):
                mensaje(request,"Error el apellido paterno debe tener caracteres alfabéticos")
                return res
            if(espacio(apellidoMaterno)):
                mensaje(request,"Error el apellido materno debe tener caracteres alfabéticos")
                return res
            if(espacio(nombreUsuario)):
                mensaje(request,"Error el nombre de usario debe tener caracteres alfabéticos")
                return res   
            if(validarTamaño(nombre,25,2)==1):
                mensaje(request,generador("Nombre",1))
                return res
            elif (validarTamaño(nombre,25,2)==2):
                mensaje(request,generador("Nombre",2))
                return res
            if(validarTamaño(apellidoPaterno,25,2)==1):
                mensaje(request,generador("apellido paterno",1))
                return res
            elif(validarTamaño(apellidoPaterno,25,2)==2):
                mensaje(request,generador("apellido paterno",1))
                return res
            if(validarTamaño(nombreUsuario,30,5)==1):
                mensaje(request,generador("nombre de usuario",1))
                return res
            elif (validarTamaño(nombreUsuario,30,5)==2):
                mensaje(request,generador("nombre de usuario",2))
                return res
            if(validarTamaño(contraseña,30,8)==1):
                mensaje(request,"Error: la contraseña debe tener un maximo de 30 caracteres" )
                return res
            elif (validarTamaño(contraseña,30,8)==2):
                mensaje(request,"Error: la contraseña debe tener un minimo de 8 caracteres")
                return res
            if(contraseña ==nombreUsuario):
                mensaje(request,"Error: La contraseña es poco segura, ¡ingrese una nueva!")
                return res
            if(Estudiante.objects.filter(usuario=nombreUsuario).exists()):
                mensaje(request,"Nombre de usuario existente")
                return res

            if(Estudiante.objects.filter(correo_estudiante=correo).exists()):
                mensaje(request,"Error: ¡Correo ya registrado! por favor ingrese un correo diferente a : "+ correo)
                return res

            if(confirmacion!=contraseña):
                mensaje(request,"La contraseña de verificacion no coincide")
                return res
            else:   
                if(valido_correo==False or not('@gmail.com' in correo) and not('@hotmail.com' in correo)and not('@outlook.com')and not('@yahoo.com')):
                    mensaje(request,"Error el correo debe estar en los siguientes dominios: gmail, hotmail, outlook, yahoo")
                    return res
                    #falta un detallito un graaaan detallito
                else:

                    mensaje(request,"todo bien ")
                    # estudiante = Estudiante(nombre_estudiante = nombre, apellidoP_estudiante = apellidoPaterno, apellidoM_estudiante = apellidoMaterno, usuario = nombreUsuario, correo_estudiante = correo, contraseña_estudiante = contraseña)
                    # estudiante.save() #ingresar datos
                    return res
        else:
            mensaje(request,"Porfavor llene todos los campos obligatorios")
            return res

    return render (request, "Formulario_Registro.html")


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
        


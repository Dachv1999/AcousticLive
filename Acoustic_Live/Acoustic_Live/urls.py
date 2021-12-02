"""Acoustic_Live URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Acoustic_Live.views import niveles, salir1,nivel_medio, nivel_avanzado,formulario_nuevoVideo, profesoresNP, profesoresNM, profesoresNA, login1,Formulario_Registro,inicio,inicio_profesores,Formulario_Registro, guardar_video_vistoBD, eliminar_video_vistoBD,formulario_editar_video,vista_editar_leccion,lista_principiante, lista_medio, lista_avanzado, crud_profesores, mover_video_arriba, mover_video_abajo, eliminar_video_profesor,Vista_Universal_Para_Profesor, recuperacion_contraseña, seccion_canciones, genero, cancion_base, cancion_ave_cristal,por_mil_noches,videogames,tratame_suavemente, ley_y_trampa,muchacha_de_risa,sangre_espanola,puerta_jardin,pensamientos,little_things,buscador,besos_guerra, vamonos_a_marte,cambiare_mi_tristeza,quiza,desde_mi_interior, vives_en_mi,cuenta_con_migo



# from gestionBD.views import lista_principiante, lista_medio, lista_avanzado, crud_profesores, mover_video_arriba, mover_video_abajo, eliminar_video_profesor,Vista_Universal_Para_Profesor


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Mis_Cursos/', niveles),
    path('Salir/', salir1),
    path('Login/', login1),
    path('Recuperar_Contra/',recuperacion_contraseña),
    path('Formulario_Registro/', Formulario_Registro),
    path('Nivel_Principiante/<int:id_profesor>/', lista_principiante),
    path('Nivel_Medio/<int:id_profesor>/', lista_medio),
    path('Nivel_Avanzado/<int:id_profesor>/', lista_avanzado),
    path('Formulario/<int:id_profesor>/', formulario_nuevoVideo),
    path('Profesores_Nivel_Principiante/', profesoresNP),
    path('Profesores_Nivel_Medio/', profesoresNM),
    path('Profesores_Nivel_Avanzado/', profesoresNA),
    path('', inicio),
    path('Inicio_Profesores/', inicio_profesores),
    path('Canciones/', seccion_canciones),
    path('buscar/', buscador),
    path('Cancion_base/<int:id_cancion>', cancion_base),
    path('guardar_db/', guardar_video_vistoBD, name='guardar_db'),
    path('eliminar_db/', eliminar_video_vistoBD, name='eliminar_db'),
    path('Subir/<int:id_profesor>/<int:orden_video>/<int:num_nivel>', mover_video_arriba),
    path('Bajar/<int:id_profesor>/<int:orden_video>/<int:num_nivel>', mover_video_abajo),
    path('Eliminar_video/<int:id_profesor>/<int:leccion_id>/<int:orden_video>/<int:nivel_leccion>', eliminar_video_profesor),
    path('Mis_Videos/<int:nivel>/',crud_profesores),
    path('Editar_video/<int:id_video>/<int:nivel>',vista_editar_leccion),
    path('validar_video_editado/<int:id_video>/<int:nivel>',formulario_editar_video),
    path('vista_videos_para_profesores/<int:id_profesor>/<int:nivel>',Vista_Universal_Para_Profesor),

    path('Genero/<int:num_genero>/', genero),
    
    
    #Canciones
    path('Ave_Cristal/', cancion_ave_cristal),
    path('airbag_por_mil_noches/',por_mil_noches),
    path('videogames/',videogames),
    path('airbag_pensamientos/',pensamientos),
    path('little_things/', little_things),
    path('tratame_suavemente/',tratame_suavemente),
    path('Ley_Y_Trampa/', ley_y_trampa),
    path('Muchacha_de_Risa/', muchacha_de_risa),
    path('Sangre_Espanola/', sangre_espanola),
    path('Puerta_Jardin/', puerta_jardin),
    path('Besos_en_Guerra/', besos_guerra),
    path('cambiare_mi_tristeza/', cambiare_mi_tristeza),
    path('Vamonos_A_Marte/', vamonos_a_marte),
    path('quizá/', quiza),
    path('desde_mi_interior/', desde_mi_interior),
    path('vives_en_mi/', vives_en_mi),
    path('cuenta_con_migo/', cuenta_con_migo),
    
    # path('Envio/', envio_formulario, name="Envio"),
]

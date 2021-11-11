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
from Acoustic_Live.views import niveles, nivel_medio, nivel_avanzado,formulario_nuevoVideo, profesoresNP, profesoresNM, profesoresNA, login,Formulario_Registro,inicio,inicio_profesores,Formulario_Registro, guardar_video_vistoBD, eliminar_video_vistoBD,formulario_editar_video,vista_editar_leccion
from gestionBD.views import lista_principiante, lista_medio, lista_avanzado, crud_profesores, mover_video_arriba, mover_video_abajo, eliminar_video_profesor,Vista_Universal_Para_Profesor


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Mis_Cursos/', niveles),
    path('Login/', login),
    path('Formulario_Registro/', Formulario_Registro),
    path('Nivel_Principiante/<int:id_profesor>/', lista_principiante),
    path('Nivel_Medio/<int:id_profesor>/', lista_medio),
    path('Nivel_Avanzado/<int:id_profesor>/', lista_avanzado),
    path('Formulario/<int:id_profesor>/', formulario_nuevoVideo),
    path('Profesores_Nivel_Principiante/', profesoresNP),
    path('Profesores_Nivel_Medio/', profesoresNM),
    path('Profesores_Nivel_Avanzado/', profesoresNA),
    path('Inicio/', inicio),
    path('Inicio_Profesores/', inicio_profesores),
    path('guardar_db/', guardar_video_vistoBD, name='guardar_db'),
    path('eliminar_db/', eliminar_video_vistoBD, name='eliminar_db'),
    path('Subir/<int:id_profesor>/<int:orden_video>/<int:num_nivel>', mover_video_arriba),
    path('Bajar/<int:id_profesor>/<int:orden_video>/<int:num_nivel>', mover_video_abajo),
    path('Eliminar_video/<int:id_profesor>/<int:leccion_id>/<int:orden_video>/<int:nivel_leccion>', eliminar_video_profesor),
    path('Mis_Videos/<int:nivel>/',crud_profesores),
    path('Editar_video/<int:id_video>/<int:nivel>',vista_editar_leccion),
    path('validar_video_editado/<int:id_video>/<int:nivel>',formulario_editar_video),
    path('vista_videos_para_profesores/<int:id_profesor>/<int:nivel>',Vista_Universal_Para_Profesor),
  


    # path('Envio/', envio_formulario, name="Envio"),
]

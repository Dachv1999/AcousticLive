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
from Acoustic_Live.views import niveles, nivel_medio, nivel_avanzado,formulario_nuevoVideo, profesoresNP, profesoresNM, profesoresNA, login
from gestionBD.views import lista_principiante, lista_medio, lista_avanzado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Mis_Cursos/', niveles),
    path('Login/', login),
    path('Nivel_Principiante/<int:id_profesor>/', lista_principiante),
    path('Nivel_Medio/<int:id_profesor>/', lista_medio),
    path('Nivel_Avanzado/<int:id_profesor>/', lista_avanzado),
    path('formulario/', formulario_nuevoVideo),
    path('Profesores_Nivel_Principiante/', profesoresNP),
    path('Profesores_Nivel_Medio/', profesoresNM),
    path('Profesores_Nivel_Avanzado/', profesoresNA),
    # path('Envio/', envio_formulario, name="Envio"),
]

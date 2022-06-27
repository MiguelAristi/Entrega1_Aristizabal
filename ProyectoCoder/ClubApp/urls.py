from django.urls import path

from .views import *

urlpatterns = [
    # URLS de ClubApp
    path('', inicio, name="inicio"),
    path('invitados/', invitados, name="invitados"),
    path('miembros/', miembros, name="miembros"),
    path('clubes/', clubes, name="clubes"),
    path('crear_club/', crear_club, name="crear_club"),
    path('crear_miembro/', crear_miembro, name="crear_miembro"),
    path('crear_invitado/', crear_invitado, name="crear_invitado"),
    path('buscar_club/', buscar_club, name="buscar_club"),
    path('buscar_miembro/', buscar_miembro, name="buscar_miembro"),
]
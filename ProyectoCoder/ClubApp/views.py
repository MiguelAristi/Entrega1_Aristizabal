from django.shortcuts import redirect, render

from .models import *
from .forms import *

# Create your views here.

def inicio(request):

    return render(request,"ClubApp/index.html",{})

def crear_club(request):

    # post
    if request.method == "POST":

        formulario = NuevoClub(request.POST)

        if formulario.is_valid():

            info_club = formulario.cleaned_data
        
            club = Club(sede=info_club["sede"],nombre=info_club["nombre"], convenio=info_club["convenio"])
            club.save() 
            
            return redirect("clubes")

        else:

            return render(request,"ClubApp/formulario_club.html",{"form":formulario})
    

    else: # get y otros

        formularioVacio = NuevoClub()

        return render(request,"ClubApp/formulario_club.html",{"form":formularioVacio})

def crear_miembro(request):

    # post
    if request.method == "POST":

        formulario = NuevoMiembro(request.POST)

        if formulario.is_valid():

            info_miembro = formulario.cleaned_data
        
            miembro = Miembro(nombre=info_miembro["nombre"], 
                              apellido=info_miembro["apellido"],
                              email=info_miembro["email"], 
                              membresia=info_miembro["membresia"])
            miembro.save() 
            
            return redirect("miembros")

        else:

            return render(request,"ClubApp/formulario_miembro.html",{"form":formulario})
    

    else: # get y otros

        formularioVacio = NuevoMiembro()

        return render(request,"ClubApp/formulario_miembro.html",{"form":formularioVacio})

def crear_invitado(request):

    # post
    if request.method == "POST":

        formulario = NuevoInvitado(request.POST)

        if formulario.is_valid():

            info_invitado = formulario.cleaned_data
        
            invitado = Invitado(nombre=info_invitado["nombre"], 
                                apellido=info_invitado["apellido"], 
                                membresia_acompanante=info_invitado["membresia_acompanante"])
            invitado.save() 
            
            return redirect("invitados")

        else:

            return render(request,"ClubApp/formulario_invitado.html",{"form":formulario})
    

    else: # get y otros

        formularioVacio = NuevoInvitado()

        return render(request,"ClubApp/formulario_invitado.html",{"form":formularioVacio})

def buscar_club(request):

    if request.method == "POST":

        club = request.POST["club"]
        
        clubes = Club.objects.filter(sede__icontains=club) 

        return render(request,"ClubApp/buscar_club.html",{"clubes":clubes})

    else: # get y otros

        clubes =  [] 
        
        return render(request,"ClubApp/buscar_club.html",{"clubes":clubes})

def buscar_miembro(request):

    if request.method == "POST":

        miembro = request.POST["miembro"]
        
        miembros = Miembro.objects.filter(membresia__icontains=miembro)

        return render(request,"ClubApp/buscar_miembro.html",{"miembros":miembros})

    else: # get y otros

        miembros =  [] 
        
        return render(request,"ClubApp/buscar_miembro.html",{"miembros":miembros})

def invitados(request):
    
    invitados = Invitado.objects.all()
    
    return render(request,"ClubApp/invitados.html",{"invitados": invitados})

def miembros(request):
    
    miembros = Miembro.objects.all()
    
    return render(request,"ClubApp/miembros.html",{"miembros":miembros})

def clubes(request):

    clubes = Club.objects.all()

    return render(request,"ClubApp/clubes.html",{"clubes":clubes})





from django import forms


class NuevoClub(forms.Form):

    sede = forms.CharField(max_length=30)
    nombre = forms.CharField(max_length=30,label="Club:")
    convenio = forms.IntegerField(min_value=0)

class NuevoMiembro(forms.Form):

    nombre = forms.CharField(max_length=30) 
    apellido = forms.CharField(max_length=30) 
    email = forms.EmailField()
    membresia = forms.IntegerField(min_value=0)

class NuevoInvitado(forms.Form):

    nombre = forms.CharField(max_length=30) 
    apellido = forms.CharField(max_length=30) 
    membresia_acompanante = forms.IntegerField(min_value=0,label="Membresia del acompañante:")
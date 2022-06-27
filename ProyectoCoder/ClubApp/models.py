from django.db import models

# Create your models here.

class Club(models.Model):

    # id por defecto
    sede = models.CharField(max_length=30) # Texto
    nombre = models.CharField(max_length=30) # Texto
    convenio = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Clubes"

class Miembro(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    apellido = models.CharField(max_length=30) # Texto
    email = models.EmailField(blank=True, null=True) # Email - Opcional
    membresia = models.IntegerField(blank=True, null=True)

class Invitado(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    apellido = models.CharField(max_length=30) # Texto
    membresia_acompanante = models.IntegerField(blank=True, null=True)




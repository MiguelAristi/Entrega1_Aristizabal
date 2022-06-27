from django.contrib import admin

from .models import *

# Register your models here.

class ClubAdmin(admin.ModelAdmin):

    list_display = ('sede','nombre', 'convenio')
    search_fields = ('sede','nombre')


class MiembroAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'membresia')


class InvitadoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido')





admin.site.register(Club, ClubAdmin)
admin.site.register(Miembro, MiembroAdmin)
admin.site.register(Invitado, InvitadoAdmin)


# admin, admin -> python manage.py createsuperuser
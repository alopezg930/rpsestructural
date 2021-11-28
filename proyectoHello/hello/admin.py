from django.contrib import admin

from .models import tessiu, paciente, distancia

# Register your models here.

class pacienteAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(paciente, pacienteAdmin)


class tessiuAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'color', 'inflammation',)

admin.site.register(tessiu, tessiuAdmin)


class distanciaAdmin(admin.ModelAdmin):
    list_display = ('r1','r2','distancia',)

admin.site.register(distancia, distanciaAdmin)

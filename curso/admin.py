from django.contrib import admin

from .models import Programa,Curso,Clase,Aula

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    pass

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    pass

@admin.register(Aula)
class ClaseAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from .models import Comentario, Entrada


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion')
    search_fields = ('titulo',)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'entrada', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('nombre', 'texto', 'entrada__titulo')
    readonly_fields = ('fecha_creacion',)

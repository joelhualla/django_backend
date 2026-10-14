from django.contrib import admin
from .models import Categoria, Receta

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'created_at')
    search_fields = ('nombre',)

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'categoria', 'dificultad', 'tiempo_preparacion_min', 'es_destacada', 'created_at')
    list_filter = ('categoria', 'dificultad', 'es_destacada')
    search_fields = ('titulo', 'descripcion', 'ingredientes')
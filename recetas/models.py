from django.db import models

class Categoria(models.Model):
    nombre = models.CharField('Nombre de Categoría', max_length=50, unique=True)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    created_at = models.DateTimeField('Fecha Creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)

    def __str__(self):
        return self.nombre


class Receta(models.Model):
    DIFICULTAD_CHOICES = [
        ('FACIL', 'Fácil'),
        ('MEDIA', 'Media'),
        ('DIFICIL', 'Difícil'),
    ]

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='recetas')
    titulo = models.CharField('Título de la Receta', max_length=100)
    descripcion = models.TextField('Descripción Breve')
    ingredientes = models.TextField('Ingredientes')
    instrucciones = models.TextField('Paso a paso de preparación')
    tiempo_preparacion_min = models.IntegerField('Tiempo preparación (minutos)', default=30)
    dificultad = models.CharField('Dificultad', max_length=10, choices=DIFICULTAD_CHOICES, default='FACIL')
    es_destacada = models.BooleanField('¿Es destacada?', default=False)
    created_at = models.DateTimeField('Fecha Creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)

    def __str__(self):
        return self.titulo
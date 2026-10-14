from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Receta
from .serializers import CategoriaSerializer, RecetaSerializer

# Vistas para la Evaluación 1 (Página de inicio y Error 404)
def home(request):
    return render(request, 'inicio.html')

def pagina_404(request, exception):
    return render(request, '404.html', status=404)

# Vistas de la API (DRF)
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
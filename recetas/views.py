from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from rest_framework import viewsets

from .models import Categoria, Receta
from .serializers import CategoriaSerializer, RecetaSerializer

# 1. Vista Pública (Página de bienvenida)
def home(request):
    return render(request, 'inicio.html')

# 2. Manejador de error 404
def pagina_404(request, exception):
    return render(request, '404.html', status=404)

# 3. Vista Protegida Basada en Función (FBV con @login_required)
@login_required
def dashboard_fbv(request):
    recetas = Receta.objects.select_related('categoria').all()
    return render(request, 'privado_fbv.html', {'recetas': recetas})

# 4. Vista Protegida Basada en Clase (CBV con LoginRequiredMixin)
class DashboardCBV(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'privado_cbv.html'
    context_object_name = 'categorias'

# 5. Vistas de la API REST (Django REST Framework)
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
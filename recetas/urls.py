from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, RecetaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'recetas', RecetaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
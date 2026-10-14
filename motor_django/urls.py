from django.contrib import admin
from django.urls import path, include
from recetas.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),          
    path('api/', include('recetas.urls')),
]

# Controlador personalizado para el error 404
handler404 = 'recetas.views.pagina_404'
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from recetas.views import home, dashboard_fbv, DashboardCBV

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas públicas
    path('', home, name='home'),
    
    # Rutas de autenticación
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Rutas privadas protegidas
    path('dashboard/fbv/', dashboard_fbv, name='dashboard_fbv'),
    path('dashboard/cbv/', DashboardCBV.as_view(), name='dashboard_cbv'),
    
    # API REST
    path('api/', include('recetas.urls')),
]

handler404 = 'recetas.views.pagina_404'
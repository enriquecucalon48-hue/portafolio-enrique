from django.contrib import admin
from django.urls import path
from portafolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('proyectos/detalle/', views.proyecto_detalle, name='proyecto_detalle'),
    path('contacto/', views.contacto, name='contacto'),
]



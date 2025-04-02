from django.urls import path

from . import views

urlpatterns = [
 # ej: /miApp/
 path('', views.index, name='index'),
 # ej: /miApp/empresas/
 path('empresas/<str:nombre_empresa>/', views.nombre, name='empresa'),
 # ej: /miApp/empresa/5/
 path('empresas/<int:id_empresa>', views.detalle, name='detalle')
]


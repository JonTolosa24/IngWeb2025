from django.urls import path
from . import views

urlpatterns = [
    path('', views.indice, name="indice"),
    path('comprar', views.comprar, name="comprar"),
    path("empresas/<str:nombre>/", views.detalle_empresa, name="empresa"),
    path("trabajadores/",views.trabajadores, name="trabajadores"),
    path("redes/",views.redes, name="redes"),
    path("empresas/",views.empresas, name="empresas"),
    path("trabajadores/<int:id>/", views.detalle_trabajador, name="detalle_trabajador"),
    path("empresa/<str:nombre_url>", views.empresa_trabajadores, name="empresa-trabajadores"),
]


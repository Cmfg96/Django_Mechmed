from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.portada, name='portada'),
    path('servicios/', views.servicios, name='servicios'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('formularioPres/', views.formulario_presupuesto, name='formulario_presupuesto'),
    path('buscar_informe/', views.buscar_informe, name='buscar_informe'),
    path('menu', views.index, name='index'),
    path('informes/', views.lista_informes, name='lista_informes'),
    path('informes/crear/', views.crear_informe, name='crear_informe'),
    path('informes/visualizar/<int:id_inf_tec>/', views.visualizar_informe, name='visualizar_informe'),
    path('informes/editar/<int:id_inf_tec>/', views.editar_informe, name='editar_informe'),
    path('informes/eliminar/<int:id_inf_tec>/', views.eliminar_informe, name='eliminar_informe'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('presupuestos/', views.presupuestos, name='presupuestos'),

    path("accounts/", include("django.contrib.auth.urls")),
]

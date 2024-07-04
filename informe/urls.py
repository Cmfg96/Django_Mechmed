from django.urls import path
from .views import index, servicios, nosotros, contacto, login, recuperar_contra, seleccion, informe_tecnico, modificar_informe, buscar_informe, formularioPres

urlpatterns = [
    path('', index, name='index'),
    path('servicios/', servicios, name='servicios'),
    path('nosotros/', nosotros, name='nosotros'),
    path('contacto/', contacto, name='contacto'),
    path('login/', login, name='login'),
    path('recuperar_contra/', recuperar_contra, name='recuperar_contra'),
    path('seleccion/', seleccion, name='seleccion'),
    path('informe_tecnico/', informe_tecnico, name='informe_tecnico'),
    path('modificar_informe/', modificar_informe, name='modificar_informe'),
    path('buscar_informe/', buscar_informe, name='buscar_informe'),
    path('formularioPres/', formularioPres, name='formularioPres'),
]
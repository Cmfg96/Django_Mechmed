from django.urls import path
from .views import index, servicios, nosotros, contacto, login

urlpatterns = [
    path('', index, name='index'),
    path('/servicios', servicios, name='servicios'),
    path('/nosotros', nosotros, name='nosotros'),
    path('/contacto', contacto, name='contacto'),
    path('/login', login, name='login'),
]
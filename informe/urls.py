from django.urls import path
from .views import index, servicios

urlpatterns = [
    path('', index, name='index'),
    path('/servicios', servicios, name='servicios'),
]
from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'informe/index.html')

def servicios(request):

    return render(request,'informe/servicios.html')

def nosotros(request):

    return render(request,'informe/nosotros.html')

def contacto(request):

    return render(request,'informe/contacto.html')

def login(request):

    return render(request,'informe/inicio_sesion.html')


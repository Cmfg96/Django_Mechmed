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

    return render(request,'informe/login.html')

def recuperar_contra(request):

    return render(request,'informe/recuperar_contra.html')

def seleccion(request):

    return render(request,'informe/seleccion.html')

def informe_tecnico(request):

    return render(request,'informe/informe_tecnico.html')

def modificar_informe(request):

    return render(request,'informe/modificar_informe.html')

def buscar_informe(request):

    return render(request,'informe/buscar_informe.html')

def formularioPres(request):

    return render(request,'informe/formularioPres.html')
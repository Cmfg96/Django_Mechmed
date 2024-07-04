from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'informe/index.html')

def servicios(request):

    return render(request,'informe/servicios.html')
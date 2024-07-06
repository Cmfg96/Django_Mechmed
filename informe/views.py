from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Informe
from .forms import InformeForm

from django.shortcuts import render

def portada(request):
    return render(request, 'informe/portada.html')

def servicios(request):
    return render(request, 'informe/servicios.html')

def nosotros(request):
    return render(request, 'informe/nosotros.html')

def contacto(request):
    return render(request, 'informe/contacto.html')

def login_view(request):
    return render(request, 'informe/login.html')

def formulario_presupuesto(request):
    return render(request, 'informe/formularioPres.html')

def buscar_informe(request):
    return render(request, 'informe/buscar_informe.html')

#------------------------------------
@login_required 
def index(request):
    request.session["usuario"]="CarlosF."
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'informe/index.html',context)

@login_required 
def informes(request):
    return render(request, 'informe/lista_informes.html')

@login_required 
def usuarios(request):
    return render(request, 'informe/usuarios.html')

@login_required 
def presupuestos(request):
    return render(request, 'informe/presupuestos.html')

@login_required 
def crear_informe(request):
    if request.method == 'POST':
        form = InformeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_informes')
    else:
        form = InformeForm()
    return render(request, 'informe/crear_informe.html', {'form': form})

@login_required 
def editar_informe(request, id_inf_tec):
    informe = get_object_or_404(Informe, id_inf_tec=id_inf_tec)
    if request.method == 'POST':
        form = InformeForm(request.POST, instance=informe)
        if form.is_valid():
            form.save()
            return redirect('lista_informes')
    else:
        form = InformeForm(instance=informe)
    return render(request, 'informe/editar_informe.html', {'form': form})
    
@login_required
def eliminar_informe(request, id_inf_tec):
    informe = get_object_or_404(Informe, id_inf_tec=id_inf_tec)
    informe.delete()
    return redirect('lista_informes')  # Asegúrate de que 'lista_informes' sea el nombre correcto de tu vista de listado

@login_required
def lista_informes(request):
    informes = Informe.objects.all()
    return render(request, 'informe/lista_informes.html', {'informes': informes})

@login_required
def visualizar_informe(request, id_inf_tec):
    informe = get_object_or_404(Informe, id_inf_tec=id_inf_tec)
    return render(request, 'informe/visualizar_informe.html', {'informe': informe})


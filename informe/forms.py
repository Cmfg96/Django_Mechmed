from django import forms
from .models import Informe

class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = [
            'descripcion',
            'estado',
            'fecha',
            'enlaces_fotos',
            'enlaces_videos',
            'id_mecanico',
            'id_cliente',
            'orden_servicio'
        ]
        

from django.db import models

class Informe(models.Model):
    id_inf_tec = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    enlaces_fotos = models.URLField(blank=True, null=True)
    enlaces_videos = models.URLField(blank=True, null=True)
    estado = models.CharField(max_length=100)
    fecha = models.DateField()
    id_cliente = models.IntegerField()
    id_mecanico = models.IntegerField()
    orden_servicio = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

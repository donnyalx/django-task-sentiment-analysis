from django.db import models
from proyectos.models import Proyectos

class Tareas(models.Model):

    ESTADO_CHOICES = [
        ("iniciada", "Iniciada"),
        ("en_proceso", "En Proceso"),
        ("terminada", "Terminada"),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    observacion_retroalimentacion = models.TextField(null=True, blank=True)
    sentimiento = models.JSONField(blank=True,null=True)
    

    class Meta:
        db_table = 'tareas'  # Nombre personalizado

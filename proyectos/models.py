from django.db import models
from django.contrib.auth.models import User 


class Proyectos(models.Model):

    ESTADO_CHOICES = [
        ("iniciada", "Iniciada"),
        ("en_proceso", "En Proceso"),
        ("terminada", "Terminada"),
    ]
    
    PRIORIDAD_CHOICES = [
        ("baja", "Baja"),
        ("media", "Media"),
        ("alta", "Alta"),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES)

    
    def __str__(self):
        return self.nombre  # Esto mostrará el nombre del proyecto

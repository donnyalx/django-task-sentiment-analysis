from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tareas
from .sentiment import analizar

@receiver(post_save, sender=Tareas)
def analizar_si_terminada(sender, instance, **kwargs):

    if (
        instance.estado == "terminada"
        and instance.observacion_retroalimentacion
        and not instance.sentimiento
    ):
        instance.sentimiento = analizar(
            instance.observacion_retroalimentacion[:800]
        )
        instance.save(update_fields=["sentimiento"])
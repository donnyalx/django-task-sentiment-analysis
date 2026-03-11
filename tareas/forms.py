from django import forms
from .models import Tareas
from proyectos import models as procesoProyectos

class TareasForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = ["nombre", "descripcion","proyecto", "fecha_inicio", "fecha_fin", "estado", "observacion_retroalimentacion"]

        labels = {
            "nombre": "Nombre",
            "descripcion": "Descripción",
            "proyecto":"Proyecto",
            "fecha_inicio": "Fecha inicial",
            "fecha_fin": "Fecha fin",
            "estado":"Estado",
            "observacion_retroalimentacion": "Observacion retroalimentacion (No obligatorio)"
        }

        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'proyecto': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)
        # Personalizar el texto por defecto del select
        self.fields['proyecto'].empty_label = "Seleccionar proyecto"  

        # Si NO tiene pk → es creación
        if not self.instance.pk:
            self.fields.pop('observacion_retroalimentacion')  

        if self.usuario:
            self.fields['proyecto'].queryset = procesoProyectos.Proyectos.objects.filter(
                usuario_id = self.usuario
            )

    def clean(self):
        cleaned_data = super().clean()
        """ Aqui invoco los valores del proyecto y comparo la fecha de inicio y fin que envio contra la minima y maxima del proyecto """
        proyecto = cleaned_data.get('proyecto')
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if proyecto and fecha_inicio:
            if fecha_inicio < proyecto.fecha_inicio:
                raise forms.ValidationError(
                    f'La fecha de inicio no puede ser anterior al inicio del proyecto ({proyecto.fecha_inicio})'
                )
            if fecha_inicio > proyecto.fecha_fin:
                raise forms.ValidationError(
                    f'La fecha de inicio no puede ser posterior al fin del proyecto ({proyecto.fecha_fin})'
                )

        if proyecto and fecha_fin:
            if fecha_fin > proyecto.fecha_fin:
                raise forms.ValidationError(
                    f'La fecha de fin no puede ser posterior al fin del proyecto ({proyecto.fecha_fin})'
                )
            
        # Validación adicional (opcional)
        if fecha_inicio and fecha_fin:
            if fecha_fin < fecha_inicio:
                raise forms.ValidationError(
                    'La fecha de fin no puede ser anterior a la fecha de inicio'
                )    

        return cleaned_data    
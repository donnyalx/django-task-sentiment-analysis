from django import forms
from .models import Proyectos

class ProyectosForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = ["nombre", "descripcion", "fecha_inicio", "fecha_fin", "estado", "prioridad"]

        labels = {
            "nombre": "Nombre",
            "descripcion": "Descripción",
            "fecha_inicio": "Fecha inicial",
            "fecha_fin": "Fecha fin",
            "estado":"Estado",
            "prioridad":"Prioridad"
        }

        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }

        """ concesionarios = procesociudadconcesionario.Concesionario.objects.all()
        ciudades = procesociudadconcesionario.Ciudad.objects.all()
        tipo_actividad = procesoactividades.TipoActividad.objects.all()
        actividad_arealizar = procesoactividades.ActividadRealizar.objects.all()
        vehiculos_promover = vehi_prom.vehiculos_promover.objects.all()

        OPCIONES_ANO = [('', 'Seleccionar'),
                        ('2025', '2025'), ('2026', '2026')]
        OPCIONES_MES = [('', 'Seleccionar'), ('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'),
                        ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')]

        Para los concesionarios
        OPCIONES_CONCESIONARIO = [('', 'Seleccionar')]
        for concesion in concesionarios:
            OPCIONES_CONCESIONARIO.append((concesion.id, concesion.nombre))

        Para la ciudades
        OPCIONES_CIUDAD = [('', 'Seleccionar')]
        for ciu in ciudades:
            OPCIONES_CIUDAD.append((ciu.id, ciu.nombre))

        Para el tipo de actividad
        OPCIONES_TIPO_ACTIVIDAD = [('', 'Seleccionar')]
        for tipo_act in tipo_actividad:
            OPCIONES_TIPO_ACTIVIDAD.append((tipo_act.id, tipo_act.nombre))

        Para la actividad_a_realizar
        OPCIONES_ACTIVIDAD_A_REALIZAR = [('', 'Seleccionar')]
        for act_a_realizar in actividad_arealizar:
            OPCIONES_ACTIVIDAD_A_REALIZAR.append(
                (act_a_realizar.id, act_a_realizar.nombre))

        Para vehiculos_promover
        OPCIONES_VEHICULOS_PROMOVER = [('', 'Seleccionar')]
        for vehi_promover in vehiculos_promover:
            OPCIONES_VEHICULOS_PROMOVER.append(
                (vehi_promover.id, vehi_promover.vehiculo))
        'ano': forms.Select(attrs={'class': 'form-control'}, choices=OPCIONES_ANO),
        widgets = {
            'concesionario': forms.Select(attrs={'class': 'form-control'}, choices=OPCIONES_CONCESIONARIO),
            'ciudad': forms.Select(attrs={'class': 'form-control'}, choices=OPCIONES_CIUDAD),
            'tipo_actividad': forms.Select(attrs={'class': 'form-control'}, choices=OPCIONES_TIPO_ACTIVIDAD),
            'actividad_a_realizar': forms.Select(attrs={'class': 'form-control'}, choices=OPCIONES_ACTIVIDAD_A_REALIZAR),
            'ano': forms.Select(attrs={'class': 'form-control'}, choices=OPCIONES_ANO),
            'mes': forms.Select(attrs={'class': 'form-control'}, choices=OPCIONES_MES),
            'vehiculos_a_promover_opc': forms.CheckboxSelectMultiple(),
            'fecha_inicial': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'fecha_final': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'alcance': forms.NumberInput(attrs={'class': 'form-control'}),
            'leads_esperados': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'title': 'Este campo debe ser mayor o igual a 0'}),
            'ventas_esperadas': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'title': 'Este campo debe ser ser mayor o igual a 0'}),
            'valor_sin_iva': forms.TextInput(attrs={'class': 'form-control'})
        }

    Esto de aqui lo vamos a usar para eliminar unas opciones de vehiculos
    vehiculos_a_promover_opc = forms.ModelMultipleChoiceField(
        queryset=vehi_prom.vehiculos_promover.objects.exclude(id__in=[12, 15]),
        widget=forms.CheckboxSelectMultiple(),
        label="Vehículos"  Esto forzará el label correcto
    )

    Hacer que el campo 'alcance' no sea obligatorio

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        Hacer que el campo 'alcance' no sea obligatorio
        self.fields['alcance'].required = False
        Desactiva la validación automática de Django
        self.fields['vehiculos_a_promover_opc'].required = False
        self.fields['vehiculos_a_promover_opc'].widget.attrs.pop(
            'required', None)

    def clean_alcance(self):
        alcance = self.cleaned_data.get('alcance')
        return alcance if alcance is not None else 0   """

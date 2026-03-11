from django.urls import path
from . import views

# Namespace para las URLs de accounts
app_name = 'tareas'

urlpatterns = [
    # Vista personalizada de registro
    path('crear-tarea/', views.crearTarea, name='crearTarea'),
    path('editar_tarea/<int:id>', views.editarTarea,
         name="editar_tarea"),
    path('eliminar_tarea/<int:id>', views.eliminarTarea,
         name="eliminar_tarea"),  
    path('ver_tareas_por_proyecto/<int:id>', views.calificaciones_tareas,
         name="ver_tareas_por_proyecto"),         
]
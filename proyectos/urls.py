from django.urls import path
from . import views

# Namespace para las URLs de accounts
app_name = 'proyectos'

urlpatterns = [
    # Vista personalizada de registro
    path('proyectos-dashboard/', views.dashboard, name='dashboard'),
    path('crear-proyecto/', views.crearProyecto, name='crearProyecto'),
    path('editar_proyecto/<int:id>', views.editarProyecto,
         name="editar_proyecto"),
    path('eliminar_proyecto/<int:id>', views.eliminarProyecto,
         name="eliminar_proyecto"),     
]
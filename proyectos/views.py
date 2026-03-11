from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProyectosForm
from django.utils.safestring import mark_safe
from .models import Proyectos
from django.db import connection
from django.core.paginator import Paginator


def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'form': ''})


def crearProyecto(request):

    print(request.user.id)

    form = ProyectosForm()

    if request.method == "POST":

        form = ProyectosForm(request.POST)

        if form.is_valid():
            # Crear la actividad sin guardarla aún, esto con el fin de modificar o cambiar datos manualmente antes 
            # de guardar la informacion
            proyecto = form.save(commit=False)
            proyecto.usuario_id = request.user.id
            proyecto.save()  # Guardar la actividad

            # Mensaje de éxito y redirección
            messages.success(
                request,
                mark_safe(
                    f'El proyecto con nombre <i>{request.POST["nombre"]}</i> ha sido creado exitosamente.')
            )

            return redirect('proyectos:crearProyecto')
        
    #Ojo aqui es donde debo cargar el listado    
    id_user = request.user.id
    with connection.cursor() as cursor:
        cursor.execute(f"""select * from proyectos_proyectos where usuario_id = {id_user} order by fecha_inicio asc""")
        proyectos = cursor.fetchall()

    lista_proyectos = [{'id': row[0], 'nombre': row[1], 'descripcion': row[2],
                       'fecha_inicio': row[3], 'fecha_fin': row[4], 'estado': row[5], 'prioridad': row[6], 'usuario_id': row[7]} for row in proyectos]
    
    paginator = Paginator(lista_proyectos, 10) 
    page_number = request.GET.get('page') 
    lista_proyectos_por_pagina = paginator.get_page(page_number)

    #return render(request, 'listado_usuarios.html', {'usuarios': lista_usuarios})    

    return render(request, 'proyectos/crear.html', {'form': form,'lista_proyectos':lista_proyectos_por_pagina})


def editarProyecto(request, id):

    proyecto = get_object_or_404(Proyectos, id=id) 

    form = ProyectosForm(instance=proyecto)

    if request.method == "POST":
        form = ProyectosForm(request.POST, instance=proyecto)

        if form.is_valid():
            # editar la actividad sin guardarla aún, esto con el fin de modificar o cambiar datos manualmente antes 
            # de guardar la informacion
            proyecto = form.save(commit=False)
            proyecto.save()
            messages.success(request, mark_safe(
                f'El proyecto <i>{proyecto.nombre}</i> ha sido actualizado exitosamente.'))
            return redirect('proyectos:crearProyecto')

    
    return render(request, 'proyectos/editar.html', {'form': form}) # Obtener la actividad


def eliminarProyecto(request, id):

    proyecto_id = id
    comprobacion = ""
    with connection.cursor() as cursor:
        try:
            cursor.execute("BEGIN;")

            cursor.execute(
                "DELETE FROM proyectos_proyectos WHERE id = %s;", [proyecto_id])
            filas_rel1 = cursor.rowcount  # Guarda cuántas filas se eliminaron

            cursor.execute("COMMIT;") 
            
            comprobacion = "eliminado"

        except Exception as e:
            cursor.execute("ROLLBACK;")  # Si hay error, deshace todo
            # return {"status": "error", "message": str(e)}
            comprobacion = "noeliminado"

    if comprobacion == "eliminado":

        messages.success(
            request,
            mark_safe(
                f'El proyecto ha sido eliminado exitosamente.')
        )

        return redirect('proyectos:crearProyecto')

    else:

        messages.success(
            request,
            mark_safe(
                f'No se ha podido eliminar el proyecto, intentelo mas tarde.')
        )

        return redirect('proyectos:crearProyecto')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TareasForm
from django.utils.safestring import mark_safe
from .models import Tareas
from django.db import connection
from django.core.paginator import Paginator
import json


def crearTarea(request):

    #print(request.user.id)

    form = TareasForm(usuario=request.user)

    if request.method == "POST":

        form = TareasForm(request.POST,usuario=request.user)

        if form.is_valid():
            # Crear la actividad sin guardarla aún, esto con el fin de modificar o cambiar datos manualmente antes 
            # de guardar la informacion
            tarea = form.save(commit=False)
            tarea.usuario_id = request.user.id
            tarea.save()  # Guardar la actividad

            # Mensaje de éxito y redirección
            messages.success(
                request,
                mark_safe(
                    f'La tarea con nombre <i>{request.POST["nombre"]}</i> ha sido creada exitosamente.')
            )

            return redirect('tareas:crearTarea')
        
    #Ojo aqui es donde debo cargar el listado    
    id_user = request.user.id
    with connection.cursor() as cursor:
        cursor.execute(f"""select * from tareas
                       inner join proyectos_proyectos on tareas.proyecto_id = proyectos_proyectos.id where proyectos_proyectos.usuario_id = {id_user} order by tareas.fecha_inicio asc""")
        tareas = cursor.fetchall()

    lista_tareas = [{'id': row[0], 'nombre': row[1], 'descripcion': row[2],
                       'fecha_inicio': row[3], 'fecha_fin': row[4], 'estado': row[5]} for row in tareas]
    
    paginator = Paginator(lista_tareas, 10) 
    page_number = request.GET.get('page') 
    lista_tareas_por_pagina = paginator.get_page(page_number)


    return render(request, 'tareas/crear.html', {'form': form,'lista_tareas':lista_tareas_por_pagina})

    #return render(request, 'tareas/crear.html', {'form': form})



def eliminarTarea(request, id):

    tarea_id = id
    comprobacion = ""
    with connection.cursor() as cursor:
        try:
            cursor.execute("BEGIN;")

            cursor.execute(
                "DELETE FROM tareas WHERE id = %s;", [tarea_id])
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
                f'La tarea ha sido eliminada exitosamente.')
        )

        return redirect('tareas:crearTarea')

    else:

        messages.success(
            request,
            mark_safe(
                f'No se ha podido eliminar el proyecto, intentelo mas tarde.')
        )

        return redirect('tareas:crearTarea')    
    

def editarTarea(request, id):

    tarea = get_object_or_404(Tareas, id=id) 

    form = TareasForm(instance=tarea)

    if request.method == "POST":
        form = TareasForm(request.POST, instance=tarea)

        if form.is_valid():
            # editar la actividad sin guardarla aún, esto con el fin de modificar o cambiar datos manualmente antes 
            # de guardar la informacion
            tarea.observacion_retroalimentacion = request.POST.get('observacion_retroalimentacion', None)
            tarea = form.save(commit=False)
            tarea.save()
            messages.success(request, mark_safe(
                f'La tarea <i>{tarea.nombre}</i> ha sido actualizada exitosamente.'))
            return redirect('tareas:crearTarea')

    
    return render(request, 'tareas/editar.html', {'form': form}) # Obtener la actividad    


def calificaciones_tareas(request,id):
    #Ojo aqui es donde debo cargar el listado    
    id_user = request.user.id


    #El nombre del proyecto
    with connection.cursor() as cursor:
        cursor.execute(f"""select nombre from proyectos_proyectos where proyectos_proyectos.id = {id}""")
        proyectosinfo = cursor.fetchall()

    for proyinfo in proyectosinfo:
        nombre_proyecto = proyinfo[0]



    with connection.cursor() as cursor:
        cursor.execute(f"""select * from tareas
                       inner join proyectos_proyectos on tareas.proyecto_id = proyectos_proyectos.id where proyectos_proyectos.id = {id} order by tareas.fecha_inicio asc""")
        tareas = cursor.fetchall()

    #Vamos a sacar los resultados de las calificaciones de sentimiento:

    lista_tareas = []

    for row1 in tareas:

        ide = row1[0]
        nombre = row1[1]
        descripcion = row1[2]
        fecha_inicio = row1[3]
        fecha_fin = row1[4]
        estado = row1[5]
        observacion = row1[7] if row1[7] else "Sin observación"

        valores = row1[8]
        if valores is not None:
            valores = json.loads(valores)
            negativo = round((valores["NEG"] * 100),2)
            neutral = round((valores["NEU"] * 100),2)
            positivo = round((valores["POS"] * 100),2)
        else:
            negativo = 0
            neutral = 0
            positivo = 0

        lista_tareas.append({
            'id': ide,
            'nombre': nombre,
            'descripcion': descripcion,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'estado': estado,
            'observacion': observacion,
            'negativo': negativo,
            'neutral': neutral,
            'positivo': positivo
        })  


    #lista_tareas = [{'id': row[0], 'nombre': row[1], 'descripcion': row[2],
    #                   'fecha_inicio': row[3], 'fecha_fin': row[4], 'estado': row[5]} for row in tareas]
    
    paginator = Paginator(lista_tareas, 10) 
    page_number = request.GET.get('page') 
    lista_tareas_por_pagina = paginator.get_page(page_number)


    return render(request, 'tareas/calificacion_tareas.html', {'lista_tareas':lista_tareas_por_pagina,'nombre_proyecto':nombre_proyecto})

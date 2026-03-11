from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def registro(request):
    """
    Vista para registrar nuevos usuarios
    Usa el formulario estándar de Django
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Crear el usuario
            user = form.save()
            username = form.cleaned_data.get('username')
            
            # Mensaje de éxito
            messages.success(request, f'Cuenta creada para {username}')
            
            # Login automático después del registro
            login(request, user)
            
            # Redireccionar al dashboard
            return redirect('proyectos:dashboard')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    """
    Vista básica de login
    """
    if request.method == 'POST':
        # Obtener datos del formulario
        username = request.POST['username']
        password = request.POST['password']
        
        # Autenticar usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login exitoso
            login(request, user)
            return redirect('proyectos:dashboard')  # O donde quieras redirigir
        else:
            # Login fallido
            messages.error(request, 'Credenciales incorrectas')
    
    # Mostrar formulario (GET o error)
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

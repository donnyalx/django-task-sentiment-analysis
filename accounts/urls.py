from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Namespace para las URLs de accounts
app_name = 'accounts'

urlpatterns = [
    # Vista personalizada de registro
    path('registro/', views.registro, name='registro'),
    # Vistas de login/logout usando las de Django
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Opcional: Cambio de contraseña (para después)
    # path('cambiar-password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('cambiar-password/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
# Sistema de Gestión de Tareas con Análisis de Sentimiento

Aplicación desarrollada con Django que permite gestionar proyectos y tareas.  
Las tareas finalizadas permiten registrar retroalimentación del usuario, la cual es analizada automáticamente mediante NLP utilizando la librería pysentimiento.

## Tecnologías

- Python
- Django
- pysentimiento
- Transformers
- Bootstrap 5
- Postgresql

## Instalación

1. Clonar repositorio

git clone https://github.com/donnyalx/django-task-sentiment-analysis.git

2. Entrar al proyecto

cd django-tareas-sentimiento

3. Crear entorno virtual

python -m venv venv

4. Activar entorno

Windows
venv\Scripts\activate

Linux/Mac
source venv/bin/activate

5. Instalar dependencias

pip install -r requirements.txt

6. Ejecutar migraciones

python manage.py migrate

7. Ejecutar servidor

python manage.py runserver

## Funcionalidades

- Gestión de proyectos
- Gestión de tareas
- Retroalimentación de tareas
- Análisis automático de sentimiento
- Visualización de métricas de sentimiento

# Proyecto Final Sistemas Distribuidos

**Integrantes:**  
  * Jose Alcivar 
  * Julio Larrea 
  * Israel Zurita
             
**Tema:**   Arquitectura de micro-servicios con caché para reducir latencia


# DJANGO API GATEWAY
Instalación
Instalar usando pip

pip install django-api-gateway
Añadir 'apigateway' y 'rest_framework' a tu paquete de INSTALLED_APPS settings.

    INSTALL_APPS = (
        ...
        'apigateway',
        'rest_framework',
    )

Añade la siguiente ruta al archivo urls.py


urlpatterns = [
    ...
    url(r'^service/', include('apigateway.urls', namespace='apigateway')),
]

Update database model

Actualiza tus modelos de base de datos

python manage.py migrate
python manage.py makemigrations

ejemplo
visita http://yourhost/admin/apigateway/api/ para añadir/editar/eliminar tus restful apis,


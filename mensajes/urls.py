from unicodedata import name
from mensajes.views import *

from django.urls import path, include

from Blog.views import *

from django.contrib.auth import views as auth_views





urlpatterns = [
    path('new/', CrearMensaje.as_view(), name='env_men'),
    path('recived/' , ver_mensajes, name='leer_men')
  

]
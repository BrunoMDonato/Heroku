from django.shortcuts import render

from mensajes.forms import *
from mensajes.models import *

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy 



# Create your views here.


class CrearMensaje(CreateView):
   
    model = Mensajes
    template_name = 'Blog/crear_mensaje.html'
    success_url= reverse_lazy ('Inicio')
    fields= '__all__'




   
def ver_mensajes (request):

    try:
        mens = Mensajes.objects.all().order_by('-fechap')
        
    except:
        mens=None
    return render (request, 'Blog/mens_rec.html', {'mens': mens})
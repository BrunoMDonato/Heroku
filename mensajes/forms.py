from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

from mensajes.models import *


# class MensajeForm(forms.ModelForm):
    

#     class Meta:
#         model = Mensajes
#         fields = [ 'receptor' , 'mensaje']

#         widgets ={
#             'receptor' : forms.ChoiceField(Mensajes),
#             'emisor': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'perf', 'type':'hidden' }),
#             'contenido': forms.Textarea( attrs={'class': 'form-control' })  
#         }


from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Mensajes(models.Model):
    
    receptor = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = RichTextField(blank=True, null=True)
    emisor = models.CharField(max_length=200)
    fechap =  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.mensaje, self.emisor)
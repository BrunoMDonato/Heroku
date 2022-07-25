from django.contrib import admin
from Blog.models import *
from mensajes.models import *

# Register your models here.

admin.site.register(Posts)
admin.site.register(Comentarios)
admin.site.register(Avatar)
admin.site.register(Mensajes)
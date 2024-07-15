from django.db import models

from datetime import date
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta

# Create your models here.
class tipoNoticia(models.Model):
    id_tipo_noticia = models.AutoField(primary_key=True)
    descripcion_tipo_noticia = models.CharField(max_length=80)

    def __str__(self):
        return self.descripcion_tipo_noticia

class NacionNoticias(models.Model):
    id_Nacion_Noticias = models.AutoField(primary_key=True)
    descripcion_Nacion_Noticias = models.CharField(max_length=80)

    def __str__(self):
        return self.descripcion_Nacion_Noticias

class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    titulo_noticia =models.CharField(max_length=80)
    decripcion_noticia = models.CharField(max_length=1000)
    fecha_noticia = models.DateField()
    imagen_noticia = models.ImageField(upload_to='core/img/', default='core/img/eventoGenerico.jpg')
    id_tipo_noticia = models.ForeignKey(tipoNoticia, on_delete=models.CASCADE, verbose_name='Tipo Noticia')
    id_Nacion_Noticias = models.ForeignKey(NacionNoticias, on_delete=models.CASCADE, verbose_name='Nacion Noticias')
    publicar_noticia = models.BooleanField(default=False)

    def __str__(self):
            return str(self.titulo_noticia)
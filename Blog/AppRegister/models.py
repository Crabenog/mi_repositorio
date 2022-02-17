from django.db import models
from django.db.models.fields import CharField

class RegistroUsuario(models.Model):
    nombreUsuario = CharField(max_length=60,null=True, blank=True)
    contraseña = CharField(max_length=60, null=True, blank=True)
    email = CharField(max_length=60,null=True, blank=True)


class Avatar(models.Model):
    user = models.ForeignKey(RegistroUsuario, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
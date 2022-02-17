from email.policy import default
import imp
from pyexpat import model
from django import forms
from django.db import models
from django.db.models.fields import CharField
from django.forms import EmailField, ImageField, URLField, URLInput
# from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    nombreUsuario = CharField(max_length=60,null=True, blank=True)
    descripcionUsuario = CharField(max_length=100,null=True, blank=True)
    linkUsuario = URLField(max_length=200)
    imagenUsuario = ImageField(max_length=100)
    emailUsuario = EmailField(max_length=254)
    contraseñaUsuario = forms.CharField(widget=forms.PasswordInput)

# class Avatar(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
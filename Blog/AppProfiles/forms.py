from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, BooleanField, EmailField, NullBooleanField, PasswordInput


class UserEditForm(UserCreationForm):
    username = CharField(label='Usuario', required=False)  
    first_name = CharField(label='Nombre', required=False)  
    last_name = CharField(label='Apellido', required=False)
    email = EmailField(required=False)
    password1 = CharField(label='Contraseña', widget=PasswordInput, required=False)
    password2 = CharField(label='Repetir Contraseña', widget=PasswordInput, required=False)
    is_staff = NullBooleanField(label='¿Es admin?')
 
    class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']
            help_texts = {k: '' for k in fields}
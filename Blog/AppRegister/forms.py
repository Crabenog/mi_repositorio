from django.forms import BooleanField, CharField, EmailField, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

    first_name = CharField(label='Nombre')  
    last_name = CharField(label='Apellido')
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repetir Contraseña', widget=PasswordInput)
    is_staff = BooleanField(label='¿Es admin?')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}
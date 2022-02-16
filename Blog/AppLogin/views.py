from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.views import LoginView

class LoginView(LoginView):
    template_name = 'login.html'

# def login_request (request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, request.POST)
        
#         if form.is_valid():
#             usuario = form.cleaned_data.get['username']
#             contraseña = form.cleaned_data.get['password']
#             user = authenticate(username=usuario, password=contraseña)
            
#             if user is not None:
#                 login(request, user)
#                 return render(request, 'inicio.html', {"mensaje":f"Bienvenido {usuario}"})
#             else:
#                 return render(request, 'login.html', {'form': form, 'error': 'No es válido el usuario y contraseña' }) 

#         else:
#             return render(request, 'login.html', {'form': form})
        
#     else:
#         form=AuthenticationForm()
#         return render(request, 'login.html', {'form': form})
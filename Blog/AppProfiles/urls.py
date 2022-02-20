from django.urls import path
from AppProfiles.views import editar_perfil

urlpatterns = [
    path('accounts/profile/', editar_perfil, name='user_editar'),
]
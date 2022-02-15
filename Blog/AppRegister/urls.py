from AppRegister.views import UserCreateView
from django.urls import path

urlpatterns = [
    path('accounts/signup/', UserCreateView.as_view(template_name='register.html'), name='register')
]
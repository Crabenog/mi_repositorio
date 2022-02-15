from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from AppLogin import views
# from AppLogin.views import login_request

urlpatterns = [
    path('login', views.login_request, name='login'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout', LogoutView.as_view(template_name='logout.html'), name='logout')
]
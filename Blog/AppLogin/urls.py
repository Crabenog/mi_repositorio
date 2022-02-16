from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # path('login', login_request, name='login'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout', LogoutView.as_view(template_name='logout.html'), name='logout')
]
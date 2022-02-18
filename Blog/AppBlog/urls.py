from django.urls import path
from .views import artistas, artistas_formulario, inicio, galeria, buscar, busqueda_artista, about_us, not_pages_yet
from AppBlog import views 
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('artistasFormulario/', artistas_formulario, name = 'artistas_formulario'),
    path('', inicio, name='inicio'),
    # path('galerias/', galeria, name='galerias'),
    path('about/', about_us, name='about_us'),
    path('artistas/', artistas, name='artistas'),
    path('buscar/', buscar, name='buscar'),
    path('busquedaArtistas/', busqueda_artista, name='busqueda_artista'),
    # path('galeriasFormulario/', galerias_formulario, name = 'galerias_formulario'),
    path('clientes/', views.ClienteListView.as_view(), name="clientes"),
    path('clientes/add', views.ClienteCreateView.as_view(), name="cliente_add"),
    path('clientes/update/<pk>', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/delete/<pk>', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('clientes/view/<pk>', views.ClienteDetailView.as_view(), name='cliente_view'),
    path('galerias/', views.GaleriaListView.as_view(), name="galerias"),
    path('galerias/add', views.GaleriaCreateView.as_view(), name="galeria_add"),
    path('galerias/update/<pk>', views.GaleriaUpdateView.as_view(), name='galeria_update'),
    path('galerias/delete/<pk>', views.GaleriaDeleteView.as_view(), name='galeria_delete'),
    path('galerias/view/<pk>', views.GaleriaDetailView.as_view(), name='galeria_view'),
    path('404', not_pages_yet, name='not_pages_yet'),
    # path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('accounts/signup/', UserCreateView.as_view(template_name='register.html'), name='register'),
    # path('accounts/logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('accounts/profile/', editar_perfil, name='user_editar'),
    path('accounts/avatar/add/', views.agregar_avatar, name='avatar_add')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
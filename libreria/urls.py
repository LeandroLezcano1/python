from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about_me', views.about_me, name='about_me'),
    path('equipos', views.equipos, name='equipos'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('equipos/crear', views.crear, name='crear'),
    path('equipos/editar', views.editar, name='editar'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

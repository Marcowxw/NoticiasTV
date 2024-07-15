from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        """Logout via GET (no recomendado, pero posible)."""
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('', index, name="index"),
    path('index', index, name="index"),
    path('login/', login_view, name='login'),
    path('registro/', registro_view, name='registro'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('administrador',vista_logueado, name='administrador'),

    path('detalles_noticia/<int:id_noticia>',detalles_noticia,name='detalles_noticia'),

    path('usuario-logueado',usuario_logueado, name='usuario-logueado'),

    #################### MANTENEDOR NOTICIAS ##################
    path('lista-noticias', lista_noticias, name='lista-noticias'),
    path('administrar-noticia', admin_noticia, name="administrar-noticia"),
    path('administrar-noticia/crear-noticia/', crear_noticia, name='crear-noticia'),
    path('administrar-noticia/editar-noticia/<int:id_noticia>/', editar_noticia, name='modificar-noticia'),
    path('administrar-noticia/eliminar-noticia/<int:id_noticia>/', eliminar_noticia, name='eliminar-noticia'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from .forms import *
from django.db.models import Value, CharField
from django.contrib.auth.views import LogoutView

from .decorators import admin_required
# Create your views here.

def index(request):
    noticias = Noticia.objects.filter(publicar_noticia=True)  # Obtiene todas las noticias
    return render(request, 'core/index.html', {'noticias': noticias})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff== True:
                return redirect('administrador')  # Redirigir a la página de inicio
            else:
                return redirect('usuario-logueado')
        else:
            return render(request, 'core/autentificacion/login.html', {'form': form})
    else:
        form = LoginForm()
        
    return render(request, 'core/autentificacion/login.html', {'form': form})

def vista_logueado(request):
    return render(request, 'core/administrador-noticias/inicio-logueado.html')

def usuario_logueado(request):
    return render(request, 'core/vista-usuario-logueado/usuario-logueado.html',{'user': request.user})

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')  # Redirigir a la página de inicio
    else:
        form = RegistroForm()
    return render(request, 'core/autentificacion/registrar.html', {'form': form})

def detalles_noticia(request, id_noticia):
    noticias = Noticia.objects.filter(id_noticia=id_noticia)  # Obtiene todas las noticias
    return render(request, 'core/detalle-noticia.html', {'noticias': noticias})


################################### MANTENEDOR NOTICIAS ###################################

def admin_noticia(request):
    return render(request, 'core/administrador-noticias/noticias/administrar-noticias.html')

def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaFormAdd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('administrar-noticia')
    else:
        form = NoticiaFormAdd()
    return render(request, 'core/administrador-noticias/noticias/crear-noticia.html', {'form': form})

def editar_noticia(request, id_noticia):
    noticias = get_object_or_404(Noticia, id_noticia=id_noticia)
    if request.method == 'POST':
        form = NoticiaFormMod(request.POST, request.FILES, instance=noticias)
        if form.is_valid():
            form.save()
            return redirect('administrar-noticia')
    else:
        form = NoticiaFormMod(instance=noticias)
    return render(request, 'core/administrador-noticias/noticias/modificar-noticias.html', {'form': form, 'noticias': noticias})

def eliminar_noticia(request, id_noticia):
    noticias = get_object_or_404(Noticia, id_noticia=id_noticia)
    if request.method == 'POST':
        noticias.delete()
        return redirect('administrar-noticia')
    return render(request, 'core/administrador-noticias/noticias/eliminar-noticias.html', {'noticias': noticias})

def lista_noticias(_request):
    noticia = []
    try:
        noticia = list(Noticia.objects.values(
            'id_noticia','titulo_noticia', 'decripcion_noticia', 'fecha_noticia', 'imagen_noticia','id_tipo_noticia__descripcion_tipo_noticia','id_Nacion_Noticias__descripcion_Nacion_Noticias'
        ).annotate(tipo_usuario=Value('Noticia', output_field=CharField())))

        ##noticia.extend(Noticia)
        data = {'noticias': noticia}
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
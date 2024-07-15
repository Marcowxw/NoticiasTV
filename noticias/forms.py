from django import forms
from .models import *
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data


########################### FORMULARIO NOTICIAS ##########################

    # titulo_noticia =models.CharField(max_length=80)
    # decripcion_noticia = models.CharField(max_length=255)
    # fecha_noticia = models.DateField()
    # imagen_noticia = models.ImageField(upload_to='core/img/', default='core/img/eventoGenerico.jpg')
    # id_tipo_noticia = models.ForeignKey(tipoNoticia, on_delete=models.CASCADE, verbose_name='Tipo Noticia')
    # id_Nacion_Noticias = models.ForeignKey(NacionNoticias, on_delete=models.CASCADE, verbose_name='Nacion Noticias')
    # publicar_noticia = models.BooleanField(default=False)

class NoticiaFormAdd(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = [
            'titulo_noticia', 'decripcion_noticia', 'fecha_noticia', 'imagen_noticia','id_tipo_noticia','id_Nacion_Noticias'
        ]
        widgets = {
            'titulo_noticia': forms.TextInput(attrs={'class': 'form-control'}),
            'decripcion_noticia': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_noticia': forms.DateInput(attrs={'class': 'form-control'}),
            'imagen_noticia': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'id_tipo_noticia': forms.Select(attrs={'class': 'form-control'}),
            'id_Nacion_Noticias': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(NoticiaFormAdd, self).__init__(*args, **kwargs)
        self.fields['id_tipo_noticia'].queryset = tipoNoticia.objects.all()
        self.fields['id_Nacion_Noticias'].queryset = NacionNoticias.objects.all()

class NoticiaFormMod(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = [
            'titulo_noticia', 'decripcion_noticia', 'fecha_noticia', 'imagen_noticia','id_tipo_noticia','id_Nacion_Noticias','publicar_noticia'
        ]
        widgets = {
            'titulo_noticia': forms.TextInput(attrs={'class': 'form-control'}),
            'decripcion_noticia': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_noticia': forms.DateInput(attrs={'class': 'form-control'}),
            'imagen_noticia': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'id_tipo_noticia': forms.Select(attrs={'class': 'form-control'}),
            'id_Nacion_Noticias': forms.Select(attrs={'class': 'form-control'}),
            'id_Nacion_Noticias': forms.Select(attrs={'class': 'form-control'}),
            'publicar_noticia': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super(NoticiaFormMod, self).__init__(*args, **kwargs)
        self.fields['id_tipo_noticia'].queryset = tipoNoticia.objects.all()
        self.fields['id_Nacion_Noticias'].queryset = NacionNoticias.objects.all()

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class PacienteRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
    fields = ['username', 'email', 'password1', 'password2']






from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['data', 'hora']

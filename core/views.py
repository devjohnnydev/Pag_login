from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Consulta, Paciente
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import redirect


from django.shortcuts import render

# Remova a importação de home se houver algum conflito
# Caso o erro ocorra aqui, remova a linha abaixo se ela existe.
# from .views import home

# Função de view para a página inicial
def home(request):
    return render(request, 'home.html')

def pagina_paciente(request):
    return render(request, 'pagina_paciente.html')

def pagina_medico(request):
    return render(request, 'pagina_medico.html')

def agendar_consulta(request):
    return render(request, 'agendar_consulta.html')

def listar_consultas(request):
    return render(request, 'listar_consultas.html')

def pagina_proprietario(request):
    return render(request, 'pagina_proprietario.html')

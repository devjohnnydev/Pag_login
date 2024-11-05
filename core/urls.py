from django.urls import path
from .views import home, pagina_paciente, pagina_medico, agendar_consulta, listar_consultas, pagina_proprietario
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),  # Rota da página inicial
    path('home/', home, name='home'),  # Manter a rota caso você tenha uma URL '/home/'
    path('paciente/', pagina_paciente, name='pagina_paciente'),
    path('home/medico/', pagina_medico, name='pagina_medico'),
    path('agendar_consulta/', agendar_consulta, name='agendar_consulta'),
    path('listar_consultas/', listar_consultas, name='listar_consultas'),
    path('proprietario/', pagina_proprietario, name='pagina_proprietario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

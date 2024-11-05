from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

class Paciente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_pacientes/', default='fotos_pacientes/default.jpg')

    def __str__(self):
        return f'Paciente: {self.usuario.username}'


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

    def clean(self):
        # Verifica se a data da consulta é uma data passada
        if self.data < timezone.now().date():
            raise ValidationError('A data da consulta não pode ser uma data passada.')

    def __str__(self):
        return f'Consulta de {self.paciente.usuario.username} em {self.data} às {self.hora}'

    class Meta:
        unique_together = ('paciente', 'data', 'hora')  # Impede consultas duplicadas para o mesmo paciente em um horário específico

"""Entidades da baseline ER-SIRE 2.1. Usuário: User padrão do Django."""
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Agencia(models.Model):
    nome = models.CharField(max_length=150)

    class Meta:
        db_table = 'sire_agencia'

    def __str__(self):
        return self.nome


class TipoPerfil(models.TextChoices):
    PASSAGEIRO = 'PASSAGEIRO', 'Passageiro'
    AGENTE = 'AGENTE', 'Agente'


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    tipo = models.CharField(max_length=20, choices=TipoPerfil.choices)
    agencia = models.ForeignKey(Agencia, null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'sire_perfil_usuario'
        constraints = [models.CheckConstraint(
            condition=(models.Q(tipo='AGENTE', agencia__isnull=False) |
                       models.Q(tipo='PASSAGEIRO', agencia__isnull=True)),
            name='perfil_agencia_compativel')]

    def clean(self):
        if self.tipo == TipoPerfil.AGENTE and not self.agencia_id:
            raise ValidationError({'agencia': 'Agente deve estar vinculado a uma agência.'})
        if self.tipo == TipoPerfil.PASSAGEIRO and self.agencia_id:
            raise ValidationError({'agencia': 'Passageiro deve permanecer sem agência.'})

    def __str__(self):
        return f'{self.usuario} — {self.get_tipo_display()}'

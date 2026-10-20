"""Entidades da baseline ER-SIRE 2.1. Usuário: User padrão do Django."""

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Agencia(models.Model):
    nome = models.CharField(max_length=150)

    class Meta:
        db_table = "sire_agencia"

    def __str__(self):
        return self.nome


class TipoPerfil(models.TextChoices):
    PASSAGEIRO = "PASSAGEIRO", "Passageiro"
    AGENTE = "AGENTE", "Agente"


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="perfil"
    )
    tipo = models.CharField(max_length=20, choices=TipoPerfil.choices)
    agencia = models.ForeignKey(
        Agencia, null=True, blank=True, on_delete=models.PROTECT
    )

    class Meta:
        db_table = "sire_perfil_usuario"
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(tipo="AGENTE", agencia__isnull=False)
                    | models.Q(tipo="PASSAGEIRO", agencia__isnull=True)
                ),
                name="perfil_agencia_compativel",
            )
        ]

    def clean(self):
        if self.tipo == TipoPerfil.AGENTE and not self.agencia_id:
            raise ValidationError(
                {"agencia": "Agente deve estar vinculado a uma agência."}
            )
        if self.tipo == TipoPerfil.PASSAGEIRO and self.agencia_id:
            raise ValidationError(
                {"agencia": "Passageiro deve permanecer sem agência."}
            )

    def __str__(self):
        return f"{self.usuario} — {self.get_tipo_display()}"


class StatusExcursao(models.TextChoices):
    RASCUNHO = "RASCUNHO", "Rascunho"
    PUBLICADA = "PUBLICADA", "Publicada"


class Excursao(models.Model):
    titulo = models.CharField(max_length=200)
    destino = models.CharField(max_length=150)
    data_saida = models.DateField()
    data_retorno = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    capacidade = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20, choices=StatusExcursao.choices, default=StatusExcursao.RASCUNHO
    )
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT)

    class Meta:
        db_table = "sire_excursao"
        ordering = ("data_saida", "id")
        constraints = [
            models.CheckConstraint(
                condition=models.Q(capacidade__gt=0), name="capacidade_positiva"
            ),
            models.CheckConstraint(
                condition=models.Q(valor__gte=0), name="valor_nao_negativo"
            ),
            models.CheckConstraint(
                condition=models.Q(status__in=["RASCUNHO", "PUBLICADA"]),
                name="status_excursao_valido",
            ),
        ]

    def clean(self):
        erros = {}
        if (
            self.data_retorno
            and self.data_saida
            and self.data_retorno < self.data_saida
        ):
            erros["data_retorno"] = "Retorno não pode ser anterior à saída."
        if self.capacidade is not None and self.capacidade <= 0:
            erros["capacidade"] = "Informe capacidade maior que zero."
        if self.valor is not None and self.valor < 0:
            erros["valor"] = "Valor não pode ser negativo."
        if (
            self.pk
            and self.capacidade is not None
            and self.capacidade < self.reservas.count()
        ):
            erros["capacidade"] = (
                "Capacidade não pode ser menor que as reservas existentes."
            )
        if erros:
            raise ValidationError(erros)

    def calcular_disponibilidade(self):
        return self.capacidade - self.reservas.count()

    def possui_vaga(self):
        return self.calcular_disponibilidade() > 0

    def pode_publicar(self):
        try:
            self.full_clean()
        except ValidationError:
            return False
        return self.status == StatusExcursao.RASCUNHO and self.pontos_embarque.exists()

    def __str__(self):
        return self.titulo


class PontoEmbarque(models.Model):
    local = models.CharField(max_length=200)
    horario = models.TimeField()
    excursao = models.ForeignKey(
        Excursao, on_delete=models.CASCADE, related_name="pontos_embarque"
    )

    class Meta:
        db_table = "sire_ponto_embarque"
        ordering = ("horario", "id")

    def __str__(self):
        return f"{self.local} — {self.horario:%H:%M}"


class Reserva(models.Model):
    data_reserva = models.DateTimeField(auto_now_add=True)
    passageiro = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="reservas_sire"
    )
    excursao = models.ForeignKey(
        Excursao, on_delete=models.PROTECT, related_name="reservas"
    )
    ponto_embarque = models.ForeignKey(PontoEmbarque, on_delete=models.PROTECT)

    class Meta:
        db_table = "sire_reserva"
        ordering = ("-data_reserva", "-id")

    def clean(self):
        perfil = (
            getattr(self.passageiro, "perfil", None) if self.passageiro_id else None
        )
        if not perfil or perfil.tipo != TipoPerfil.PASSAGEIRO:
            raise ValidationError("Reserva exige perfil Passageiro.")
        if (
            self.ponto_embarque_id
            and self.ponto_embarque.excursao_id != self.excursao_id
        ):
            raise ValidationError(
                {"ponto_embarque": "Escolha um embarque desta excursão."}
            )
        if self.excursao_id and self.excursao.status != StatusExcursao.PUBLICADA:
            raise ValidationError("A excursão não está publicada.")
        if not self.pk and self.excursao_id and not self.excursao.possui_vaga():
            raise ValidationError("Não há vagas disponíveis.")

    def __str__(self):
        return f"Reserva {self.pk} — {self.excursao}"

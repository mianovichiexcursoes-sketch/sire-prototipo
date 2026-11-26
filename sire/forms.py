"""Formulários de conta, catálogo e operações de excursão e reserva."""

from datetime import date

from django import forms
from django.conf import settings
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from django.utils.safestring import mark_safe

from . import recuperacao
from .destinos import DESTINOS, padronizar_destino
from .models import Excursao, PerfilUsuario, PontoEmbarque, TipoPacote, TipoPerfil


class LoginSireForm(AuthenticationForm):
    error_messages = {
        **AuthenticationForm.error_messages,
        "invalid_login": "Usuário ou senha inválidos. Confira os dados e tente novamente.",
    }

    def clean_username(self):
        username = self.cleaned_data["username"]
        variantes = User.objects.filter(username__iexact=username).values_list(
            "username", flat=True
        )
        nomes = list(variantes[:2])
        # Só resolve um nome alternativo se houver uma única conta possível.
        # Com colisão, o Django ainda pode autenticar a grafia exata.
        return nomes[0] if len(nomes) == 1 else username


class RecuperacaoSenhaForm(PasswordResetForm):
    def clean_email(self):
        if not settings.SIRE_RESET_DOMAIN:
            raise forms.ValidationError("A recuperação por e-mail não está disponível neste ambiente.")
        return self.cleaned_data["email"]

    def get_users(self, email):
        return (
            user for user in super().get_users(email)
            if not recuperacao.conta_compartilhada(user)
        )

    def save(self, **kwargs):
        kwargs.update(domain_override=settings.SIRE_RESET_DOMAIN, use_https=True)
        super().save(**kwargs)


class RecuperacaoPorCodigoForm(forms.Form):
    """Usuário + código de recuperação + senha nova (sem e-mail)."""

    ERRO = "Usuário ou código de recuperação inválidos."

    username = forms.CharField(label="Usuário", max_length=150)
    codigo = forms.CharField(
        label="Código de recuperação",
        max_length=40,
        help_text="O código mostrado quando a conta foi criada. Com ou sem hífens.",
    )
    new_password1 = forms.CharField(
        label="Senha nova",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="Confirmação da senha nova",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    def clean(self):
        dados = super().clean()
        if self.errors:
            return dados
        # Mesma regra do login: a grafia alternativa só vale para conta única.
        contas = list(User.objects.filter(username__iexact=dados["username"])[:2])
        if len(contas) == 2:
            contas = [c for c in contas if c.username == dados["username"]]
        usuario = contas[0] if len(contas) == 1 else None
        if (
            usuario is None
            or not usuario.is_active
            or recuperacao.conta_compartilhada(usuario)
            or not recuperacao.confere(usuario, dados["codigo"])
        ):
            # Uma única mensagem: não revela se o usuário existe.
            raise forms.ValidationError(self.ERRO)
        if dados["new_password1"] != dados["new_password2"]:
            self.add_error("new_password2", "As duas senhas não são iguais.")
            return dados
        try:
            password_validation.validate_password(dados["new_password1"], usuario)
        except forms.ValidationError as erro:
            self.add_error("new_password1", erro)
            return dados
        self.usuario = usuario
        return dados

    def save(self):
        self.usuario.set_password(self.cleaned_data["new_password1"])
        self.usuario.save(update_fields=["password"])
        return self.usuario


class CadastroPassageiroForm(UserCreationForm):
    # O e-mail é obrigatório e único para que a recuperação de senha (extensão,
    # fora da baseline) funcione para toda conta nova. Usa o campo email já
    # existente no User do Django: não há campo, tabela ou migration novos.
    email = forms.EmailField(
        label="E-mail",
        help_text="Obrigatório. Usado para recuperar a senha.",
    )

    # Extensão: dado usado pela agência para identificar o passageiro.
    data_nascimento = forms.DateField(
        label="Data de nascimento",
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
    )
    aceite = forms.BooleanField(
        label=mark_safe(
            'Li o <a href="/privacidade/" target="_blank" rel="noopener">aviso de '
            "privacidade</a> e concordo com o uso dos meus dados para as reservas."
        ),
        error_messages={"required": "É preciso concordar com o aviso de privacidade."},
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")

    field_order = (
        "username",
        "first_name",
        "last_name",
        "email",
        "data_nascimento",
        "password1",
        "password2",
        "aceite",
    )

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Já existe uma conta com este e-mail.")
        return email

    def clean_data_nascimento(self):
        nascimento = self.cleaned_data["data_nascimento"]
        hoje = date.today()
        if nascimento > hoje:
            raise forms.ValidationError("A data de nascimento não pode estar no futuro.")
        if nascimento.year < hoje.year - 120:
            raise forms.ValidationError("Informe uma data de nascimento válida.")
        return nascimento

    @transaction.atomic
    def save(self, commit=True):
        if not commit:
            return super().save(commit=False)
        usuario = super().save()
        PerfilUsuario.objects.create(
            usuario=usuario,
            tipo=TipoPerfil.PASSAGEIRO,
            data_nascimento=self.cleaned_data["data_nascimento"],
        )
        return usuario


class FiltroCatalogoForm(forms.Form):
    destino_catalogo = forms.ChoiceField(
        label="Qual destino?", required=False,
    )
    destino = forms.CharField(
        label="Busca livre por destino",
        required=False,
        max_length=150,
        widget=forms.TextInput(
            attrs={"id": "destino", "placeholder": "Digite um destino"}
        ),
    )
    saida_de = forms.DateField(
        label="Saída a partir de",
        required=False,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
    )
    saida_ate = forms.DateField(
        label="Saída até",
        required=False,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
    )
    tipo_pacote = forms.ChoiceField(
        label="Tipo de pacote",
        required=False,
        choices=[("", "Todos os tipos"), *TipoPacote.choices],
    )

    palavra_chave = forms.CharField(
        label="Palavra-chave", required=False, max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "Nome ou roteiro da viagem"}),
    )
    embarque = forms.ChoiceField(label="Onde quer embarcar?", required=False)
    duracao = forms.ChoiceField(
        label="Quanto tempo quer viajar?", required=False,
        choices=[("", "Qualquer duração"), ("1", "1 dia"), ("2_3", "2 a 3 dias"),
                 ("4", "4 dias ou mais")],
    )
    ordem = forms.ChoiceField(
        label="Ordenar por", required=False,
        choices=[("", "Data de saída"), ("preco", "Menor preço"),
                 ("preco_desc", "Maior preço")],
    )

    def __init__(self, *args, destinos=(), embarques=(), **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["destino_catalogo"].choices = [("", "Todos os destinos")] + [
            (d, d) for d in destinos
        ]
        self.fields["embarque"].choices = [("", "Todos os embarques")] + [
            (e, e) for e in embarques
        ]

    def clean(self):
        dados = super().clean()
        inicio, fim = dados.get("saida_de"), dados.get("saida_ate")
        if inicio and fim and inicio > fim:
            self.add_error(
                "saida_ate", "A data final deve ser igual ou posterior à data inicial."
            )
        return dados


class ExcursaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.destinos_predefinidos = DESTINOS
        self.fields["destino"].widget.attrs.update({"list": "destinos-predefinidos"})
        self.fields["destino"].help_text = (
            "Selecione uma sugestão ou informe um destino ainda não listado."
        )

    def clean_destino(self):
        return padronizar_destino(self.cleaned_data["destino"])

    class Meta:
        model = Excursao
        fields = (
            "titulo",
            "destino",
            "tipo_pacote",
            "descricao",
            "roteiro",
            "inclusos",
            "data_saida",
            "data_retorno",
            "valor",
            "capacidade",
        )
        help_texts = {
            "tipo_pacote": "Opcional. Deixe em branco para manter sem classificação.",
            "descricao": "Opcional. Apresente os principais detalhes do pacote.",
            "roteiro": "Opcional. Informe os horários e paradas do roteiro.",
            "inclusos": "Opcional. Escreva um item incluso por linha.",
        }
        widgets = {
            "descricao": forms.Textarea(attrs={"rows": 4, "maxlength": 4000}),
            "roteiro": forms.Textarea(attrs={"rows": 6, "maxlength": 8000}),
            "inclusos": forms.Textarea(attrs={"rows": 5, "maxlength": 4000}),
            "data_saida": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "data_retorno": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        }


class FotoExcursaoForm(forms.Form):
    foto = forms.FileField(
        label="Foto da excursão",
        # accept: o seletor do sistema já mostra só imagens; data-limite-bytes é
        # usado por fotos-upload.js para avisar antes de enviar.
        widget=forms.FileInput(
            attrs={"accept": "image/jpeg,image/png,image/webp", "data-limite-bytes": 5 * 1024 * 1024}
        ),
        help_text=(
            "JPG, PNG ou WebP. Até 5 MB. O sistema ajusta o tamanho antes de enviar ao "
            "Drive. Não envie fotos em que pessoas possam ser identificadas."
        ),
    )

    def clean_foto(self):
        foto = self.cleaned_data["foto"]
        if foto.size > 5 * 1024 * 1024:
            raise forms.ValidationError("A foto deve ter no máximo 5 MB.")
        if foto.size == 0:
            raise forms.ValidationError("A foto não pode estar vazia.")
        return foto


class PontoEmbarqueForm(forms.ModelForm):
    class Meta:
        model = PontoEmbarque
        fields = ("local", "horario")
        widgets = {"horario": forms.TimeInput(format="%H:%M", attrs={"type": "time"})}


class ReservaForm(forms.Form):
    ponto_embarque = forms.ModelChoiceField(
        queryset=PontoEmbarque.objects.none(),
        label="Ponto de embarque",
        empty_label="Selecione o embarque",
    )

    def __init__(self, *args, excursao, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["ponto_embarque"].queryset = excursao.pontos_embarque.all()

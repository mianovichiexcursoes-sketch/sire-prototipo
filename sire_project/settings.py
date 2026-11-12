"""Configurações do protótipo acadêmico SIRE.

Sem variáveis de ambiente, o projeto roda como na entrega original: SQLite,
DEBUG ligado e acesso somente local. PostgreSQL e a demonstração publicada são
ativados por variáveis de ambiente ou por um arquivo `.env` (ver `.env.example`).
"""

import os
from pathlib import Path
from urllib.parse import unquote, urlparse

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent


def _carregar_env(caminho):
    """Lê pares CHAVE=valor de um `.env` local, sem sobrepor o ambiente real."""
    if not caminho.is_file():
        return
    for linha in caminho.read_text(encoding="utf-8-sig").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#") or "=" not in linha:
            continue
        chave, valor = linha.split("=", 1)
        os.environ.setdefault(chave.strip(), valor.strip().strip("\"'"))


def _lista(nome, padrao=""):
    return [v.strip() for v in os.environ.get(nome, padrao).split(",") if v.strip()]


_carregar_env(BASE_DIR / ".env")

# Opcional (Windows): quando o Controle de Aplicativo bloqueia a DLL embutida no
# pacote psycopg-binary, o driver usa a libpq da instalação oficial do PostgreSQL.
_libpq_dir = os.environ.get("SIRE_LIBPQ_DIR", "")
if _libpq_dir and Path(_libpq_dir).is_dir():
    os.environ["PATH"] = _libpq_dir + os.pathsep + os.environ.get("PATH", "")
    os.environ.setdefault("PSYCOPG_IMPL", "python")

DEBUG = os.environ.get("SIRE_DEBUG", "1") == "1"

_CHAVE_LOCAL = "somente-desenvolvimento-local-sire-nao-usar-em-producao"
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", _CHAVE_LOCAL)
if not DEBUG and SECRET_KEY == _CHAVE_LOCAL:
    raise ImproperlyConfigured(
        "Com SIRE_DEBUG=0, defina DJANGO_SECRET_KEY com uma chave própria."
    )

ALLOWED_HOSTS = _lista("SIRE_ALLOWED_HOSTS", "127.0.0.1,localhost")
CSRF_TRUSTED_ORIGINS = _lista("SIRE_CSRF_TRUSTED_ORIGINS")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "sire",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sire_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "sire_project.wsgi.application"
ASGI_APPLICATION = "sire_project.asgi.application"

if not DEBUG:
    # Demonstração publicada: arquivos estáticos pelo WhiteNoise e HTTPS no proxy.
    MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = os.environ.get("SIRE_SSL_REDIRECT", "1") == "1"
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


def _banco():
    """SQLite (padrão, entrega original) ou PostgreSQL, conforme o ambiente."""
    url = os.environ.get("DATABASE_URL", "")
    motor = os.environ.get("SIRE_DB_ENGINE", "sqlite").lower()
    if url:
        partes = urlparse(url)
        return {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": unquote(partes.path.lstrip("/")),
            "USER": unquote(partes.username or ""),
            "PASSWORD": unquote(partes.password or ""),
            "HOST": partes.hostname or "",
            "PORT": str(partes.port or ""),
            "CONN_MAX_AGE": 60,
        }
    if motor in ("postgresql", "postgres"):
        return {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("SIRE_DB_NAME", "sire"),
            "USER": os.environ.get("SIRE_DB_USER", "sire"),
            "PASSWORD": os.environ.get("SIRE_DB_PASSWORD", ""),
            "HOST": os.environ.get("SIRE_DB_HOST", "localhost"),
            "PORT": os.environ.get("SIRE_DB_PORT", "5432"),
        }
    return {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ.get("SIRE_SQLITE_PATH") or BASE_DIR / "db.sqlite3",
        # Serializa gravações antes da leitura da capacidade (SQLite).
        "OPTIONS": {"transaction_mode": "IMMEDIATE", "timeout": 10},
    }


DATABASES = {"default": _banco()}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_URL = "sire:login"
LOGIN_REDIRECT_URL = "sire:catalogo"
LOGOUT_REDIRECT_URL = "sire:catalogo"

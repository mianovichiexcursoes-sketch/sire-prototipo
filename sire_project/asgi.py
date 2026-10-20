"""Ponto de entrada ASGI do projeto SIRE."""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sire_project.settings")
application = get_asgi_application()

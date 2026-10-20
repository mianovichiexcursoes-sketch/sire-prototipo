"""Ponto de entrada WSGI do projeto SIRE."""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sire_project.settings")
application = get_wsgi_application()

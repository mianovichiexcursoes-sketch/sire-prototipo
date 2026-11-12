#!/usr/bin/env bash
# Build da demonstração publicada (executado pela hospedagem, em Linux).
set -o errexit

pip install -r requirements-deploy.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py criar_demo

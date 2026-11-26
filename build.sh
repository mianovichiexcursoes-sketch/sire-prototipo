#!/usr/bin/env bash
# Build da demonstração publicada (executado pela hospedagem, em Linux).
set -o errexit

pip install -r requirements-deploy.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py criar_demo
# Portfólio (saídas de dez/2026 e jan/2027). Idempotente; uma falha aqui
# não deve impedir a publicação do site.
python manage.py carregar_portfolio || echo "Aviso: portfólio não carregado nesta publicação."

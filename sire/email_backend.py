"""Envio dos e-mails de recuperação pela API HTTPS do Resend."""

import json
from urllib.error import URLError
from urllib.request import Request, urlopen

from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend


class ResendBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        enviados = 0
        for mensagem in email_messages:
            dados = {
                "from": mensagem.from_email,
                "to": mensagem.to,
                "subject": mensagem.subject,
                "text": mensagem.body,
            }
            requisicao = Request(
                "https://api.resend.com/emails",
                data=json.dumps(dados).encode(),
                headers={
                    "Authorization": f"Bearer {settings.SIRE_RESEND_API_KEY}",
                    "Content-Type": "application/json",
                    "User-Agent": "SIRE/1.0",
                },
                method="POST",
            )
            try:
                with urlopen(requisicao, timeout=10):
                    enviados += 1
            except URLError:
                if not self.fail_silently:
                    raise RuntimeError("Falha no envio de e-mail pelo provedor.") from None
        return enviados

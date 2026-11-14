"""Envio dos e-mails de recuperação pela API HTTPS do Resend."""

import json
import logging
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend

logger = logging.getLogger("sire.email")


class ResendBackend(BaseEmailBackend):
    """Envia cada mensagem por POST e registra o resultado, sem o destinatário."""

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
                with urlopen(requisicao, timeout=10) as resposta:
                    enviados += 1
                    logger.info("E-mail aceito pelo provedor (HTTP %s).", resposta.status)
            except HTTPError as erro:
                # O provedor respondeu, mas recusou: o motivo vem no corpo.
                motivo = erro.read().decode("utf-8", "replace")[:300]
                logger.error("Provedor recusou o envio: HTTP %s — %s", erro.code, motivo)
                if not self.fail_silently:
                    raise RuntimeError("O provedor recusou o envio do e-mail.") from None
            except URLError as erro:
                logger.error("Falha de rede ao contatar o provedor: %s", erro.reason)
                if not self.fail_silently:
                    raise RuntimeError("Falha de rede no envio do e-mail.") from None
        return enviados

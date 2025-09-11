from plyer import notification

import time


def criarlembrete(mensagem, segundos):
    time.sleep(segundos)

    notification.notify(
        title = "LEMBRETE",
        message = "HENRIQUE VIADO",
        timeout = 5
    )

criarlembrete("Teste123", 2)

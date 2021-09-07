from defaults import HEADERS, MAX_SEND_TRIES

import requests


def send_message(to_url, message_by, message):
    payload = {"username": message_by, "content": message}

    send_tries = 0
    while send_tries <= MAX_SEND_TRIES:
        try:
            requests.post(to_url, headers=HEADERS, json=payload)
            break

        except:
            send_tries += 1

    else:
        pass

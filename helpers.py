from defaults import *
import requests


def send_message_to_discord(webhook, message_by, message):
    payload = {"username": message_by, "content": message}

    send_tries = 0
    while send_tries <= MAX_SEND_TRIES:
        try:
            requests.post(webhook, headers=HEADERS, json=payload)
            break

        except:
            send_tries += 1

    else:
        pass


def handle_wadc_bridge(config: dict, form_title: str, form_text: str):
    payload_title = form_title
    parsed_title = [x.strip() for x in payload_title.split(":") if x.strip() != ""]
    payload_text = f"```{form_text}```"
    sender = parsed_title[-1] if len(parsed_title) >= 2 else "Unknown"

    for title in config["ignore-title-list"]:
        if title in payload_title:
            return

    for webhook_data in config["webhook-list"]:
        if webhook_data["title"] in payload_title:
            send_message_to_discord(webhook_data["webhook"], sender, payload_text)

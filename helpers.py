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


def handle_wadc_bridge(form):
    payload_title = form.get("title")
    parsed_title = [x.strip() for x in payload_title.split(":") if x.strip() != ""]
    payload_text = f"```{form.get('text')}```"
    sender = parsed_title[-1] if len(parsed_title) >= 2 else "Unknown"

    for title in IGNORE_TITLES:
        if title in payload_title:
            return

    if "TSDC SYBSc. CS (OFFICIAL)" in payload_title:
        send_message_to_discord(
            OFFICIAL_BSCCS_DC_WEBHOOK, sender, payload_text)

    elif "BSC CS" in payload_title:
        send_message_to_discord(UNOFFICIAL_BSCCS_DC_WEBHOOK, sender, payload_text)

    elif "Core Java SY BSC CS" in payload_title:
        send_message_to_discord(CORE_JAVA_DC_WEBHOOK, sender, payload_text)

    elif "DBMS SY BSC CS" in payload_title:
        send_message_to_discord(DBMS_DC_WEBHOOK, sender, payload_text)

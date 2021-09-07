from defaults import OFFICIAL_BSCCS_DC_WEBHOOK, UNOFFICIAL_BSCCS_DC_WEBHOOK
from helpers import send_message

from flask import Flask, request, jsonify
from threading import Thread
import json
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "AutoReply server v1.0"})


@app.route("/official-bsccs-dc-bridge", methods=["POST"])
def official_bsccs_dc_bridge():
    data = json.loads(request.data)

    message = f"""
```
{data["senderMessage"]}

> {datetime.fromtimestamp(int(int(data["messageDateTime"])/1000))}
```
    """

    thread = Thread(target=send_message, args=[
                    OFFICIAL_BSCCS_DC_WEBHOOK, data["senderName"], message
                    ])
    thread.start()

    return jsonify({"data": []})


@app.route("/unofficial-bsccs-dc-bridge", methods=["POST"])
def unofficial_bsccs_dc_bridge():
    data = json.loads(request.data)

    message = f"""
```
{data["senderMessage"]}

> {datetime.fromtimestamp(int(int(data["messageDateTime"])/1000))}
```
    """

    thread = Thread(target=send_message, args=[
                    UNOFFICIAL_BSCCS_DC_WEBHOOK, data["senderName"], message
                    ])
    thread.start()

    return jsonify({"data": []})

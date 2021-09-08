from helpers import handle_wadc_bridge

from flask import Flask, request, jsonify
from threading import Thread
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "AutoReply server v1.0"})


@app.route("/wadc-bridge", methods=["POST"])
def wadc_bridge():
    print(f"Received: {request.form}")

    thread = Thread(target=handle_wadc_bridge, args=[request.form])
    thread.start()

    return ('', 204)


@app.route("/test", methods=["POST"])
def test():
    print(request.data)
    print(request.form)

    return ('', 204)

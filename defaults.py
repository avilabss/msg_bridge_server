import json
from functools import lru_cache


@lru_cache()
def get_config():
    with open("./config.json", "r") as config_file:
        return json.loads(config_file.read())


HEADERS = {"content-type": "application/json"}
MAX_SEND_TRIES = 3

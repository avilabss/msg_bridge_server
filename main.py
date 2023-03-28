from fastapi import FastAPI, Form, Depends
from typing import Optional

from helpers import handle_wadc_bridge, get_config


app = FastAPI(
    title="OxyProxy Node Backend",
    openapi_url=None,
    docs_url=None,
    redoc_url=None,
)


@app.get("/")
def home():
    return {"message": "Message Bridge Server v1.2 ✨"}


@app.post("/discord/", status_code=204)
def wadc_bridge(
    name: Optional[str] = Form(None),
    pkg: Optional[str] = Form(None),
    title: Optional[str] = Form(None),
    text: Optional[str] = Form(None),
    subtext: Optional[str] = Form(None),
    bigtext: Optional[str] = Form(None),
    infotext: Optional[str] = Form(None),
    config: dict = Depends(get_config)
):
    print(f"Received: {title} - {text}")
    handle_wadc_bridge(config, title, text)
    return ""

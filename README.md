# Config.json
A config.json file is required. Create the file and add following configs:
```json
{
    "webhook-list": [
        {"title": "Your message title to detect", "webhook": "Webhook url to send when this title is detected"}
    ],
    "ignore-title-list": ["Ignore this title"]
}
```

`Example 01:`
```json
{
    "webhook-list": [
        {"title": "W2D", "webhook": "https://discord.com/api/webhooks/Jais755gh"}
    ],
    "ignore-title-list": ["WhatsApp"]
}
```

`Example 02:`
```json
{
    "webhook-list": [
        {"title": "W2D", "webhook": "https://discord.com/api/webhooks/Jais755gh"}
        {"title": "Dave", "webhook": "https://discord.com/api/webhooks/kona87sab"}
    ],
    "ignore-title-list": ["WhatsApp"]
}
```

# Run
1. Install dockder
2. Execute command: `make run`

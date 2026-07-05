import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_photo(photo_url, caption, button_url):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    keyboard = {
        "inline_keyboard": [
            [
                {
                    "text": "🛒 Buy Now",
                    "url": button_url
                }
            ]
        ]
    }

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "photo": photo_url,
            "caption": caption,
            "parse_mode": "HTML",
            "reply_markup": __import__("json").dumps(keyboard)
        }
    )

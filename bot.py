import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = """
🔥 DailyLoot Test

✅ Bot is working!

Soon I'll automatically post Amazon deals here.

Stay tuned 🚀
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})

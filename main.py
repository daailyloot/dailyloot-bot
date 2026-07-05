from deal_fetcher import fetch_deals
from filters import is_good_deal, deal_score
from affiliate import add_affiliate_tag
from telegram_sender import send_photo
from database import already_posted, mark_posted
import time


def run():
    deals = sorted(
        fetch_deals(),
        key=lambda x: deal_score(x),
        reverse=True
    )

    for deal in deals:

        if not is_good_deal(deal):
            continue

        if already_posted(deal["id"]):
            continue

        affiliate_link = add_affiliate_tag(deal["url"])

        caption = f"""🔥 <b>{deal['title']}</b>

⭐ {deal['rating']} ({deal['reviews']} Reviews)

💰 ₹{deal['price']}
📉 {deal['discount']}% OFF

🏆 Deal Score: {deal_score(deal)}/100
"""

        send_photo(
            deal["image"],
            caption,
            affiliate_link
        )

        mark_posted(deal["id"])

        time.sleep(5)


if __name__ == "__main__":
    run()

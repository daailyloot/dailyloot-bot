from deal_fetcher import fetch_deals
from filters import is_good_deal
from affiliate import add_affiliate_tag
from telegram_sender import send_photo
from database import already_posted, mark_posted


def run():
    deals = fetch_deals()

    for deal in deals:

        if not is_good_deal(deal):
            continue

        if already_posted(deal["id"]):
            continue

        affiliate = add_affiliate_tag(deal["url"])

        caption = f"""🔥 <b>{deal['title']}</b>

⭐ {deal['rating']} ({deal['reviews']} reviews)

💰 ₹{deal['price']}
📉 {deal['discount']}% OFF
"""

        send_photo(
            deal["image"],
            caption,
            affiliate
        )

        mark_posted(deal["id"])


if __name__ == "__main__":
    run()

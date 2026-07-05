from config import MIN_DISCOUNT, MIN_RATING, MIN_REVIEWS

def is_good_deal(product):
    return (
        product["discount"] >= MIN_DISCOUNT
        and product["rating"] >= MIN_RATING
        and product["reviews"] >= MIN_REVIEWS
    )

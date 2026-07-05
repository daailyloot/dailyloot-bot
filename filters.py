from config import MIN_DISCOUNT, MIN_RATING, MIN_REVIEWS

def is_good_deal(product):
    return (
        product["discount"] >= MIN_DISCOUNT
        and product["rating"] >= MIN_RATING
        and product["reviews"] >= MIN_REVIEWS
    )

def deal_score(product):
    discount_score = min((product["discount"] / 70) * 50, 50)
    rating_score = (product["rating"] / 5) * 30
    review_score = min((product["reviews"] / 1000) * 20, 20)

    total = discount_score + rating_score + review_score

    return round(min(total, 100), 1)

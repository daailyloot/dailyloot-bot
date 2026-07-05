from urllib.parse import urlparse, parse_qs, urlencode

AFFILIATE_TAG = "daailyloot-21"

def add_affiliate_tag(url):
    if "tag=" in url:
        return url

    separator = "&" if "?" in url else "?"

    return f"{url}{separator}tag={AFFILIATE_TAG}"

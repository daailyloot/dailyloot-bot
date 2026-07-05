import json
import os

DB_FILE = "posted_deals.json"

def load_posted():
    if not os.path.exists(DB_FILE):
        return []

    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_posted(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def already_posted(product_id):
    return product_id in load_posted()

def mark_posted(product_id):
    data = load_posted()

    if product_id not in data:
        data.append(product_id)
        save_posted(data)

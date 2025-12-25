import json

def recommend_hotel(city):
    with open("data/hotels.json", "r") as f:
        hotels = json.load(f)

    city_hotels = [h for h in hotels if h["city"].lower() == city.lower()]

    if not city_hotels:
        return None

    return min(city_hotels, key=lambda x: x["price_per_night"])

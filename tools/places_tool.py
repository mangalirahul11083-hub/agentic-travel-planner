import json

def get_places(city):
    with open("data/places.json", "r") as f:
        places = json.load(f)

    city_places = [p for p in places if p["city"].lower() == city.lower()]

    # Sort by rating (highest first)
    city_places.sort(key=lambda x: x["rating"], reverse=True)

    return city_places

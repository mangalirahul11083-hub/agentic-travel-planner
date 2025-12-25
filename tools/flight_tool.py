import json

def get_all_routes():
    with open("data/flights.json", "r") as f:
        flights = json.load(f)
    return flights

def search_flight(source, destination):
    flights = get_all_routes()

    valid = [
        f for f in flights
        if f["from"].lower() == source.lower()
        and f["to"].lower() == destination.lower()
    ]

    if not valid:
        return None

    return min(valid, key=lambda x: x["price"])

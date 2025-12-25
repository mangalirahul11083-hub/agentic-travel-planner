from tools.flight_tool import search_flight
from tools.hotel_tool import recommend_hotel
from tools.places_tool import get_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget

def travel_agent(source, destination, days):
    flight = search_flight(source, destination)
    if flight is None:
        return None

    hotel = recommend_hotel(destination)
    if hotel is None:
        return None

    places = get_places(destination)
    weather = get_weather(days)

    itinerary = []
    for i in range(days):
        if i < len(places):
            itinerary.append(f"Day {i+1}: Visit {places[i]['name']}")
        else:
            itinerary.append(f"Day {i+1}: Free exploration")

    budget = estimate_budget(
        flight["price"],
        hotel["price_per_night"],
        days
    )

    return {
        "flight": flight,
        "hotel": hotel,
        "weather": weather,
        "itinerary": itinerary,
        "budget": budget
    }

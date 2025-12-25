def estimate_budget(flight_price, hotel_price, days):
    food_travel = 1000 * days
    total = flight_price + (hotel_price * days) + food_travel

    return {
        "flight": flight_price,
        "hotel": hotel_price * days,
        "food_travel": food_travel,
        "total": total
    }

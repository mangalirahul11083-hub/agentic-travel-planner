from agent.travel_agent import travel_agent

print("=== AI Travel Planning Assistant ===")

source = input("Source city: ")
destination = input("Destination city: ")
days = int(input("Number of days: "))

result = travel_agent(source, destination, days)

print("\n--- Trip Plan ---")

print("\nFlight Selected:")
print(result["flight"])

print("\nHotel Recommended:")
print(result["hotel"])

print("\nWeather Forecast:")
for i, temp in enumerate(result["weather"], 1):
    print(f"Day {i}: {temp}°C")

print("\nItinerary:")
for item in result["itinerary"]:
    print(item)

print("\nBudget Breakdown:")
for k, v in result["budget"].items():
    print(f"{k.capitalize()}: ₹{v}")

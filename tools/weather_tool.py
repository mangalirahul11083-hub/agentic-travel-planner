import requests

def get_weather(days):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=20.5937&longitude=78.9629"
        "&daily=temperature_2m_max&timezone=auto"
    )
    data = requests.get(url).json()
    return data["daily"]["temperature_2m_max"][:days]

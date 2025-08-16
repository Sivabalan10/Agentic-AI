import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_current_weather(location: str) -> dict:
    """
    Tool Name: get_current_weather

    Description:
        This tool retrieves the current weather information for a specified location using the OpenWeatherMap API.
        It takes a location string (such as a city name or "City,CountryCode") as input and returns weather data in JSON format.
        The tool requires an environment variable 'WEATHER_API_KEY' to be set with a valid OpenWeatherMap API key.

    Inputs:
        - location (str): The name of the city or "City,CountryCode" (e.g., "London,UK").

    Outputs:
        - dict: A dictionary containing the weather data for the specified location, or an error message if the request fails.
        - response like this below:
        {'coord': {'lon': 80.1182, 'lat': 13.0015}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 28.09, 'feels_like': 32.81, 'temp_min': 28.09, 'temp_max': 28.09, 'pressure': 1009, 'humidity': 83, 'sea_level': 1009, 'grnd_level': 1006}, 'visibility': 10000, 'wind': {'speed': 4.44, 'deg': 178, 'gust': 7.59}, 'clouds': {'all': 100}, 'dt': 1754756347, 'sys': {'country': 'IN', 'sunrise': 1754699190, 'sunset': 1754744622}, 'timezone': 19800, 'id': 1264527, 'name': 'Thandalam', 'cod': 200}
    Usage Example:
        weather = get_current_weather("Thandalam")
        print(weather)

    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": os.getenv("WEATHER_API_KEY"),
        "units": "metric"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

# Example usage:
weather = get_current_weather("Thandalam")
print(weather)

# ...existing code...

# In-memory database of persons
PERSON_DATABASE = [
    {
        "name": "Sivabalan T",
        "email": "221501138@rajalakshmi.edu.in",
        "character_info": "Curious, hardworking, and passionate about AI.",
        "location": ",Thandalam, Chennai, India"
    },
    {
        "name": "Yudeeswaran",
        "email": "221501182@rajalakshmi.edu.in",
        "character_info": "Curious, staying in hostel, Focusing on placement, AI enthusiast, always using phone, lean",
        "location": "Thandalam, Chennai, India"
    },
    {
        "name": "Shrinithi",
        "email": "221501135@rajalakshmi.edu.in",
        "character_info": "Staying in home with family, Care taker, commited, hosnest girl, cute face, focusing on career and boyfriend",
        "location": "Poonamalle, Chennai, India"
    },
    {
        "name": "Sriram",
        "email": "221501135@rajalakshmi.edu.in",
        "character_info": "Curious, staying in hostel, always using phone, health worst, in medication, gym boy, GATE preparation, Love failure",
        "location": "Thandalam, Chennai, India"
    },
    {
        "name": "Sharukesh",
        "email": "221501130@rajalakshmi.edu.in",
        "character_info": "Hard worker, non stop talker, studying for placement, not focusing on health, late night sleep",
        "location": "Thandalam, Chennai, India"
    },
    # Add more person records as needed
]

def get_person_info(name: str) -> dict:
    """
    Tool Name: get_person_info
    Available names: Sivabalan T, Yudeeswaran, Shrinithi, Sharukesh, Sriram
    Description:
        This tool retrieves information about a person from the in-memory database based on the provided name.
        It returns the person's name, email, character_info, and location if found.

    Inputs:
        - name (str): The name of the person to search for.

    Outputs:
        - dict: A dictionary containing the person's data if found, or an error message if not found.

    Usage Example:
        person = get_person_info("Sivabalan T")
        print(person)
    """
    for person in PERSON_DATABASE:
        if person["name"].lower() == name.lower():
            return person
    return {"error": f"No data found for name: {name}"}

# Example usage:
# person = get_person_info("Sivabalan T")
# print(person)
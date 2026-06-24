import requests
import random


def calculator(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Calculation Error: {e}"


import requests

def weather_tool(query):
    try:
        city = query.lower().replace("weather", "").strip()

        if city == "":
            city = "delhi"

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )

        data = response.json()

        current = data["current_condition"][0]

        return f"""
Weather Report

City : {city.title()}
Temperature : {current['temp_C']} °C
Feels Like : {current['FeelsLikeC']} °C
Humidity : {current['humidity']} %
Wind Speed : {current['windspeedKmph']} km/h
Condition : {current['weatherDesc'][0]['value']}
"""

    except Exception as e:
        return f"Weather Error: {str(e)}"


def github_tool(query):
    try:
        username = query.split()[-1]

        url = f"https://api.github.com/users/{username}"

        response = requests.get(url, timeout=10)
        data = response.json()

        if "message" in data:
            return "GitHub user not found"

        return f"""
Name : {data.get('name')}
Username : {data.get('login')}
Followers : {data.get('followers')}
Following : {data.get('following')}
Public Repositories : {data.get('public_repos')}
Profile URL : {data.get('html_url')}
"""

    except Exception as e:
        return f"GitHub Error: {e}"


def railway_tool(query):
    return """
Railway Information

Train Number : 12951
Status : Running
Delay : 10 Minutes
Platform : 3
"""


def parking_tool(query):
    return """
Parking Availability

Zone A : 32 Slots Available
Zone B : 18 Slots Available
Zone C : 11 Slots Available
"""


def traffic_tool(query):
    return """
Traffic Report

Traffic Level : Moderate
Average Speed : 42 km/h
Congestion Index : 58%
"""


def hospital_tool(query):
    return """
Nearby Hospitals

1. Apollo Hospital
2. City Hospital
3. Government Medical Center
"""


def police_tool(query):
    return """
Nearby Police Stations

1. Central Police Station
2. Sector 17 Police Station
"""


def news_tool(query):
    return """
Latest News Module Ready

Real News API can be connected later.
"""


def fuel_tool(query):
    return """
Fuel Prices

Petrol : ₹95/L
Diesel : ₹88/L
"""


def ev_station_tool(query):
    return """
Nearest EV Charging Station

Distance : 2.5 km
Available Chargers : 4
"""


def sensor_tool(query):

    temperature = random.randint(25, 40)
    humidity = random.randint(40, 80)
    aqi = random.randint(50, 150)
    parking = random.randint(10, 100)
    noise = random.randint(30, 90)

    return f"""
Sensor Dashboard

Temperature : {temperature} °C
Humidity : {humidity} %
AQI : {aqi}
Parking Occupancy : {parking} %
Noise Level : {noise} dB
"""


def resume_tool(query):
    return "Resume Analysis Tool Activated"


def portfolio_tool(query):
    return "Portfolio Builder Tool Activated"


def research_tool(query):
    return "Research Tool Activated"


def pdf_tool(query):
    return "PDF Analyzer Tool Activated"


def image_tool(query):
    return "Image Analyzer Tool Activated"


def code_tool(query):
    return f"Code Generation Request: {query}"
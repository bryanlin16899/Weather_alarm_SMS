import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
MY_API_KEY = "964fcfec612a63e1860c42f376fc1f90"

weather_params = {
    "lat": 24.147736,
    "lon": 120.673645,
    "appid": MY_API_KEY,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        print("Bring an umbrella.")
# print(data["hourly"][0]["weather"][0]["id"])

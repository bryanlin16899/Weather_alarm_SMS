import os
import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
MY_API_KEY = "964fcfec612a63e1860c42f376fc1f90"
MY_PHONENUMBER = "+886972988302"

weather_params = {
    "lat": -1.237927,
    "lon": 116.852852,
    "appid": MY_API_KEY,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    account_sid = 'AC54eaf9f436c566420931df8dbbb038a8'
    auth_token = '0d8456dcb3755e650a5a8e30dc22bd29'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an umbrella.",
        from_="+13603287144",
        to=MY_PHONENUMBER
    )
    print(message.sid)
    print("GOGO")
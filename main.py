import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
MY_API_KEY = "964fcfec612a63e1860c42f376fc1f90"

weather_params = {
    "lat": 24.147736,
    "lon": 120.673645,
    "appid": MY_API_KEY

}


response = requests.get(OWN_Endpoint, params=weather_params)
print(response.json())

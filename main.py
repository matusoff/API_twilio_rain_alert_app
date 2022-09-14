import requests
#import os
from twilio.rest import Client

account_sid = "AC5d78048cd29e10629ccdb5a16aa75e78"
auth_token = "24ec3658a2c1993d0bf5b7e4f47add97"


Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

api_key = "6a65d07699f449f3365a3d85ec1ba0ea"


parameters = {
    "lat": 45.501690,
    "lon": -73.567253,
    "appid": api_key,
    "exclude": "current,minutely,dayly"
}

response = requests.get(Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

#to go through th json file use [] like in the code line below
# print(weather_data["hourly"][0]["weather"][0]["id"])

#slice the data until 12 hours
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
         body="It's going to rain today, take an umbrella",
         from_="+14014969474",
         to="+15146924631"

     )
    print(message.status)





import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = "get your account_sid number from twilio" # https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages-python
auth_token = "get your auth_token from twilio"


Endpoint = "https://api.openweathermap.org/data/2.5/onecall"  # Endpoint API 

api_key = "get your api_key from https://api.openweathermap.org"


parameters = {
    "lat": xxxxxxxx, #place here the Latitude  coordinates of your city from https://www.latlong.net/
    "lon": xxxxxxxx, #place here the Longitude coordinates of your city from https://www.latlong.net/
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
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
    .create(
         body="It's going to rain today, take an umbrella ☔",
         from_="get your trial phone number from twilio",
         to="add here your phone number or number where you want to receive the sms alert, you have to verify it from twilio""

     )
    print(message.status)

#take the code and place it in https://www.pythonanywhere.com in order to get the automated message to your phone 


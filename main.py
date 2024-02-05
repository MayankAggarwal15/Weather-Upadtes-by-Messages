# PROJECT ON WEATHER FORECASTING VIA SMS

import geocoder
import requests
from twilio.rest import Client

# ------------------------------- WEATHER API ------------------------------ #

api_key = "YOUR API KEY"
api_endpoint = "https://api.openweathermap.org/data/2.5/weather"

g = geocoder.ip('me')
latitude = g.latlng[0]
longitude = g.latlng[1]

print(latitude, longitude)

my_latitude = latitude
my_longitude = longitude

parameters = {
    "lat" : my_latitude,
    "lon" : my_longitude,
    "appid" : api_key
}

response = requests.get(api_endpoint , params=parameters)
response.raise_for_status()

weather_data = response.json()

weather_id = weather_data['weather'][0]['id']
weather_condition = weather_data['weather'][0]['main']
description = weather_data['weather'][0]['description']
temperature = weather_data['main']['temp']
feels_like = weather_data['main']['feels_like']


# ------------------------------- TWILIO ------------------------------ #

account_sid = "YOUR TWILIO ACCOUNT SID"
auth_token = "YOUR TWILIO ACCOUNT AUTH TOKEN"

client = Client(account_sid, auth_token)

from_number = "+19513389092"
to_number = 'YOUR NUMBER'

text_msg = f'''
        WEATHER UPDATE

Weather Condition : {weather_condition}
Temperature : {temperature - 274.15 :.2f}℃

Feels like : {feels_like - 274.15 :.2f}℃

Description : {description}'''


if weather_id < 700:

    message = client.messages.create(
        body=f"{text_msg}\nIT'S RAINY TODAY. REMEMBER TO TAKE AN UMBRELLA ☂ ",
        from_= from_number,
        to= to_number
        )

else :

    message = client.messages.create(
        body= text_msg,
        from_= from_number,
        to= to_number
        )
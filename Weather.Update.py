#!/usr/bin/env python3
from twilio.rest import (Client)
import keys
import requests


API_KEY = "____"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Cochran"


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY + "&units=imperial"

response = requests.get(url).json()
data = response

 # data retrieved from openweathermap.org

sky_image = data['weather'][0]['description'].capitalize()
temperature_f = data['main']['temp']
humidity = data['main']['humidity']
weather_info = (f"Temperature: {temperature_f}\u00b0F " 
                f"Humidity Level: {humidity}% "
                f"Sky: {sky_image}")




# twilio id and numbers

account_sid = '______'
auth_token = '_____'

twilio_number = '____'
target_number = '____'

client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(
    body='Here is the weather for today! '+ weather_info,
    from_=keys.twilio_number,
    to=keys.target_number
)
print(message.body)

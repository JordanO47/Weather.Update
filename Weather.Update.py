#!/usr/bin/env python3
from twilio.rest import (Client)
import keys
import requests


API_KEY = "5968f0303201c12403b102bee97046d6"
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

account_sid = 'ACe284ba79fd2003fac5d94c53c37710aa'
auth_token = 'd92085afa05a1a9b429ef8358a799be2'

twilio_number = '+18662798804'
target_number = '+19125152268'

client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(
    body='Here is the weather for today! '+ weather_info,
    from_=keys.twilio_number,
    to=keys.target_number
)
print(message.body)

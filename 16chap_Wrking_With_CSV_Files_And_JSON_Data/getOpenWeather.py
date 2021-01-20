#! python3
# getOpenWeather.py - Prints the weather for a location from the command line
APPID = 'f8c51ac08fb738a82a43aee2b3ee4637'

import json, requests, sys
# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city, 2-letter_coutry_code')
    sys.exit()

location = ''.join(sys.argv[1:])
# Download the JSON data from OpenWeatherMap.org's API.
url='https://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()
#print(response.text)
# Load JSON data into a Python variable
weatherData = json.loads(response.text)
# Print weather descriptions
w=weatherData['weather']
e= weatherData['main']
celsius = int(e['temp']) - 273.5 
print(f'Current weather in {location}')
print(w[0]['main'],'-', w[0]['description'])
print(f'{celsius}')

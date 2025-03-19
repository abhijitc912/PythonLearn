import requests

city= input ("For which city do you want to check the weather?")

url="http://api.weatherapi.com/v1/current.json?key=5c0f85ab979d4738a28181346251803&q="+city+"&aqi=no"

response= requests.get(url)

weather = response.json()

temp = weather.get('current').get('temp_c')
condition = weather.get('current').get('condition').get('text')

print ("Today's weather in",city,"is", condition,"and the temperature is",temp,"degree Celcius")
import json
import urllib.request, urllib.parse, urllib.error


api_key = '101963c92f086ffd48d59bcdea7c0af8'
url = 'https://api.openweathermap.org/data/2.5/weather?q='
city = 'Coimbatore'
appid = '&units=metric&appid=' + api_key
final_url = url + city + appid
#print(final_url)
fh = urllib.request.urlopen(final_url).read().decode()
data = json.loads(fh)
print(json.dumps(data, indent =2))
temp = data["main"]["temp_min"]
weather = data["weather"][0]["description"]
print(temp, weather)

import json
import urllib.request, urllib.parse, urllib.error

url = 'https://official-joke-api.appspot.com/random_joke'
fh = urllib.request.urlopen(url).read().decode()
data = json.loads(fh)
#print(data)
try:
    print("Setup: ", data['setup'])
    print("Punchline: ",data['punchline'])
    print(type(data['setup']))
except:
    print("Not Working")

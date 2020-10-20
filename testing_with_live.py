import speech_recognition as sr
import os
import pyttsx3
import json
import urllib.request, urllib.parse, urllib.error
import playsound
from gtts import gTTS
r = sr.Recognizer()
'''roger = pyttsx3.init()
roger.setProperty('rate', 150)
voices = roger.getProperty('voices')
roger.setProperty('voice', 'english_us')

#roger.say("This is Roger, How may I help you?")
#roger.runAndWait()
'''

def speak(text):
    tts = gTTS(text=text, lang='en',slow=False)
    filename ='speech.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    #roger.say(text)
    #roger.runAndWait()

speak("This is Linda, How may I help you?")

def weather(city):
    api_key_weather = '101963c92f086ffd48d59bcdea7c0af8'
    url = 'https://api.openweathermap.org/data/2.5/weather?q='
    appid = '&units=metric&appid=' + api_key_weather
    final_url = url + city + appid
    fh = urllib.request.urlopen(final_url).read().decode()
    data = json.loads(fh)
    #print(json.dumps(data, indent =2))
    temp = data["main"]["temp_min"]
    weather = data["weather"][0]["description"]
    print(temp, weather)
    condition = "Temperature is "+ str(temp) + " degree celcius and" + "Weather condition is" + weather
    speak(condition)

def joke():
    url = 'https://official-joke-api.appspot.com/random_joke'
    fh = urllib.request.urlopen(url).read().decode()
    data = json.loads(fh)
    setup = data['setup']
    punchline = data['punchline']
    print(setup)
    speak(setup)
    print(punchline)
    speak(punchline)

while(1):
    try:
        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text.capitalize())

            if (text == "show files"):
                os.system("ls -l")
                speak("These are the files")

            if (text == "update"):
                os.system("echo %s | sudo -s apt-get update" % ("rugved"))  # -s for reading from STDIN
                speak("The system is updated")

            if( text == "play music"):
                speak("Playing favorite songs from Spotify")

            if( text == "tell me a joke"):
                joke()

            if (text.find("weather") != -1):
                city = text.split()[5]
                print(city)
                weather(city)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")

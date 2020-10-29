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
    tts = gTTS(text=text, lang='en-uk',slow=False)
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
def dictionary(word):
    url = 'https://api.dictionaryapi.dev/api/v2/entries/'
    lang_code = 'en'
    #word = 'new'
    final_url = url + lang_code + '/' + word
    #print(final_url)
    fh = urllib.request.urlopen(final_url).read().decode()
    data = json.loads(fh)
    #print(json.dumps(data, indent =2))
    #print(data[0]["meanings"][0]["definitions"][0]["definition"])
    definition = data[0]["meanings"][0]["definitions"][0]["definition"]
    print(definition)
    speak("Definition:")
    speak(definition)
    meaning_len =  len(data[0]["meanings"][0]["definitions"][0]["synonyms"])
    meaning = data[0]["meanings"][0]["definitions"][0]["synonyms"][0:2]
    speak("Its synonyms are:" + meaning[0] + meaning[1])
    #speak(meaning[0])
    #speak(meaning[1])
    print(meaning)

while(1):
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text.capitalize())

            if (text == "show files"):
                os.system("ls -l")
                speak("These are the files")

            elif (text == "update"):
                os.system("echo %s | sudo -s apt-get update" % ("*****"))  # -s for reading from STDIN Enter Password
                speak("The system is updated")

            elif( "play music" in text):
                speak("Playing songs from rhythmbox")
                os.system('rhythmbox-client  --play')
            elif ("next song" in text):
                speak("Playing Next song")
                os.system('rhythmbox-client  --next')
            elif ("stop song" in text):
                speak("Pausing song")
                os.system('rhythmbox-client  --pause')

            elif( "joke" in text):
                joke()

            elif( "meaning" in text):
                #print("Working")
                word = text.split()[-1]
                dictionary(word)
            elif (text.find("weather") != -1):
                city = text.split()[5]
                print(city)
                weather(city)


    except sr.RequestError as e:
        #print("Could not request results; {0}".format(e))
        continue
    except sr.UnknownValueError:
        continue
        #print("unknown error occured")

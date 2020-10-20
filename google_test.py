from gtts import gTTS
import playsound

def speak(text):
    tts = gTTS(text=text, lang='en',slow=False)
    filename ='speech.mp3'
    tts.save(filename)
    playsound.playsound(filename)


speak("These are the files")

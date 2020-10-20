import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 175)     # setting up new voice rate
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male

#engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
engine.setProperty('voice', 'english_us')
engine.say('These are the files')
engine.runAndWait()
'''
for voice in voices:
    # to get the info. about various voices in our
        print("Voice:")
        print("ID: %s" %voice.id)
        print("Name: %s" %voice.name)
        print("Age: %s" %voice.age)
        print("Gender: %s" %voice.gender)
        print("Languages Known: %s" %voice.languages)
        engine.setProperty('voice', voice.id)  # changes the voice
        engine.say('The quick brown fox jumped over the lazy dog.')
        engine.runAndWait()
'''
#engine.runAndWait()
#rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate

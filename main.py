import speech_recognition as sr 
import webbrowser as web
from time import ctime
import time
import playsound
from gtts import gTTS 
import random
import os
rec = sr.Recognizer() # for recognizing speech
#
# helper function for Speaking
#
def allen_speak(audio_text):
    tts = gTTS(text=audio_text, lang='en')
    rnd_number = random.randint(1,1000000)
    audio_file = 'audio-'+str(rnd_number)+'.mp3' # making audio file
    tts.save(audio_file) # saving audio file
    playsound.playsound(audio_file) # playing the audio
    print(audio_text) # printing audio text
    os.remove(audio_file) # removing audio file that is created above
#
# Helper function for recording voice and get text from that audio
#
def record_voice(ask = False):
    allen_speak('How can I help you?')
    with sr.Microphone() as source: # source is out microphone
        if(ask):
            allen_speak(ask)
        audio = rec.listen(source) # listening from source microphone
        voice_text = ''
        try:
            voice_text = rec.recognize_google(audio) # converto audio to text
        except sr.UnknownValueError:
            allen_speak('Sorry, I did not understand...')
        except sr.RequestError:
            allen_speak('Sorry, My speech service is down...')
        return voice_text
#
# helper function for reponses
#
def response(voice_data): 
    if('what is your name' in voice_data):
        allen_speak('My name is Allen')
    if('how old are you' in voice_data):
        allen_speak('I am 21 years old')
    if('what time is it' in voice_data):
        allen_speak(ctime())
    if('search' in voice_data):
        search = record_voice('What do you want to search?')
        search_url = 'https://google.com/search?q='+search
        web.get().open(search_url)
        allen_speak('Here is what I found on google')
    if('find location' in voice_data):
        location = record_voice('What is the location?')
        search_url = 'https://google.nl/maps/place/'+location+'&amp;'
        web.get().open(search_url)
        allen_speak('Here is the location of '+ location)
    if('exit' in voice_data):
        exit()

time.sleep(1)
while True:
    voice_data = record_voice()  # recording audio and get text
    response(voice_data) # responses

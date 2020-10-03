import time
import pyttsx3
from PyDictionary import PyDictionary
import webbrowser
import wikipedia
import geocoder
from pygeocoder import Geocoder
import datetime
import alsaaudio
import os,subprocess
m = alsaaudio.Mixer()
i=0
engine=pyttsx3.init()

def runScript():
    while True:
        time.sleep(2)
        import speech_recognition as sr
        r = sr.Recognizer()
        r.dynamic_energy_thresold=False
        old=False
        with sr.Microphone() as source:
            print("Say something!")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        print("fetching")
        try:
            input1=r.recognize_google(audio)
            print("You said: " + input1)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            continue
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            continue 
        if input1=="hello Calvin" and i==0:
            print("Hello peeps !! How can i help you ??")
            engine = pyttsx3.init()
            engine.say("Hi peeps How can i help you ")
            engine.runAndWait()
            i=1
            continue
        else:
            if i==0:
                print("Sorry plz say hello Calvin!!! for start the assistant ")
                continue
            else:
                pass
        if input1=="bye bye":
            exit()
        elif input1[0:10]=="set volume":
            try:
                a=int(input1[11:])
                m.setvolume(a)
                print("volume is set to",a)
            except (ValueError,alsaaudio.ALSAAudioError):
                print("volume is bet 0 and 100 ")
                continue

        elif input1=="mute volume":
            m.setvolume(0)
        elif input1=="hello Calvin" or input1=="hello Kelvin" or input1=="hello" or input1=="hi":
            print("Hi Manit !! How can i help you ??")
            engine.say("Hi Manit How can i help you ")
            engine.runAndWait()
        elif input1=="who is your father":
            print("I was raised by engineer Manit Choudhary")
            engine.say("I was raised by engineer Manit Choudhary")
            engine.runAndWait()
            continue
        elif input1=="what is the current time" or input1=="what is the time now":
            print(datetime.datetime.now().time())
            engine.say(datetime.datetime.now().time())
            engine.runAndWait()
        elif input1=="what is the date today" or input1=="what is the today date":
            print(datetime.datetime.today().strftime('%m/%d/%Y'))
            engine.say(datetime.datetime.today().strftime('%m/%d/%Y'))
            engine.runAndWait()

        elif input1=="what is your name" or input1=="tell me about you" or input1=="who are you" or input1=="tell me your name":
            print("My name is Calvin . I am a assistant ")
            engine.say("My name is Calvin . I am a assistant")
            engine.runAndWait()
        elif input1=="how are you":
            print("I am fine as you . Anything i can do for you !")
            engine.say("I am fine as You anything i can do for you ")
            engine.runAndWait()
        elif input1=="what are you doing" or input1=="what are you doing now":
            print("I'm preety much always learning new things")
            engine.say("I'm preety much always learning new things")
            engine.runAndWait()
        elif input1=="what is my location" or input1=="where are you now" or input1=="tell me about my location":
            g = geocoder.ip('me')
            location = Geocoder.reverse_geocode(g.lat,g.lng)
            print ("City:",location.city)
            print ("Country:",location.country)
            engine.say("Current City is ")
            engine.say(location.city)
            engine.say("Current Country is")
            engine.say(location.country)
            engine.runAndWait()

        elif input1[0:13]=="tell me about":
            ny = wikipedia.summary(input1[14:],sentences=2)
            print(ny)
            engine.say(ny)
            engine.runAndWait()
        elif input1[0:22]=="Wikipedia search about":
            webbrowser.open('https://en.wikipedia.org/wiki/{}'.format(input1[23:]),new=2)
        elif input1[0:6]=="who is":
            ny = wikipedia.page(input1[7:])
            print(ny.content[0:400])
            engine.say(ny.content[0:400])
            engine.runAndWait()
        

        elif input1=="open YouTube":
            print("opening youtube...")
            engine.say("opening youtube..")
            engine.runAndWait()
            webbrowser.open('https://www.youtube.com',new=2)

        elif input1=="open gana.com":
            print("opening ganna.com...")
            engine.say("opening ganna.com..")
            engine.runAndWait()
            webbrowser.open('https://gaana.com/song/jitni-dafa',new=2)
        elif input1=="open VLC" or input1=="open vlc player":
            print("opening vlc player...")
            engine.say("opening vlc player..")
            engine.runAndWait()
            subprocess.Popen("vlc")


        elif input1[0:22]=="what is the meaning of":
            try:
                dictionary=PyDictionary()
                word=input1[23:]
                print(word)
                ans=dictionary.meaning(word)
                print(ans)
                engine = pyttsx3.init()
                engine.say("It means ")
                engine.say(ans)
                engine.runAndWait()
            except sr.UnknownValueError:
                continue
        else:
            webbrowser.open('https://www.google.com/search?source=hp&ei=2oMfW4eqA4fbvASGjLXIDw&q={}&oq={}&gs_l=psy-ab.3..35i39k1j0l2j0i131k1j0j0i131k1l3j0i67k1j0.22610.23535.0.23911.8.6.0.0.0.0.233.233.2-1.1.0....0...1.1.64.psy-ab..7.1.232.0...0.XhDxSrWUE1Q'.format(input1,input1), new=2)
            time.sleep(4)

if __name__ = "__main__":
    runScript()
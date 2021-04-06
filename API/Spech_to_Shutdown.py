import pyttsx3
import speech_recognition as sr
import os


def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    import time
    time.sleep(2)
    return Query


def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


Speak("Do you want to shutdown your computer sir?")
while True:
    command = take_commands()
    if "no" in command:
        Speak("Thank u sir I will not shut down the computer")
        break
    if "yes" in command:
        Speak("Shutting the computer")
        os.system("shutdown /s /t 30")
        break
    Speak("Say that again sir")

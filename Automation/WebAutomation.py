import webbrowser
import pyttsx3
import speech_recognition as sr

#######################################Google Search#######################################
# X = input("What do you want to search?\n")
# webbrowser.open("https://www.google.com/search?q="+X)

#######################################Text to speech#######################################
# def say(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
#
#
# say(
#     "Hello Joe Biden. I am Abu Bakkar Siddik. I'm from Dhaka, Bangladesh. I'm your big fan. i would like to see you the next American President. Thank You ")


#######################################speech to Text#######################################

# def waitForCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening........")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     try:
#         print("Recongnizing the Voice........")
#         query = r.recognize_google(audio, language="en-in")
#         print(query)
#     except Exception as e:
#         print(e)
#         print("say it Clearly......")
#         return "None"
#     return query
#
#
# while True:
#     waitForCommand()


import smtplib
from email.message import EmailMessage

EmailAdd = "a.sanjida2020@gmail.com"  # senders Gmail id over here
Pass = "01639474727"  # senders Gmail's Password over here

msg = EmailMessage()
msg['Subject'] = 'Subject of the Email'  # Subject of Email
msg['From'] = EmailAdd
msg['To'] = 'a.sanjida2020@gmail.com'  # Reciver of the Mail
msg.set_content('Mail Body')  # Email body or Content

#### >> Code from here will send the message << ####
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Added Gmails SMTP Server
    smtp.login(EmailAdd, Pass)  # This command Login SMTP Library using your GMAIL
    smtp.send_message(msg)  # This Sends the message


""" 
Functionalities:
    1. Searches anything from wikipedia
    just include "Wikipedia" in the word
    2. Plays different genre of songs like
    if you speak "play favourite songs" it plays 
    favourite songs from the specified directory,
    if you speak "play silent songs" it plays 
    silent songs from the specified directory,
    3. also wishes the user


"""


from email.mime import audio
from logging import exception
from random import random
from re import X
from tkinter import Label
from unittest import result
from winreg import QueryInfoKey
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("GOOD Morning TEJAS! ")
    elif hour >=12 and hour<18:
        speak("GOOD Afternoon TEJAS! ")
    else:
        speak("GOOD Evening TEJAS! ")
    
    speak("IT'S ME, YOUR MATE POWER! How may I help you ?")

def takeCommand():
    '''It takes microphone input and returns string output '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        # r.energy_threshold()
        print("Listening... ")
        r.pause_threshold = 1
        audio= r.listen(source)
    try:
        print("Recoginzing...")
        query = r.recognize_google(audio)
        print(f"User Said : {query}\n")
    except Exception as e:
        print("sorry, Can You Repeat")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('tejasbhutada4976@gmail.com', 'tejaschuha007')
    server.sendmail('tejasbhutada4976@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    wishMe()
    
    # Logic For Executing Tasks based on query
    while True:
    # if 1:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 4)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("Youtube.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")
        
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        
        elif "play favourite songs" in query:
            music_dir = "D:\\songs\\favourite songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif "play silent songs" in query:
            music_dir= "D:\\songs\\silent songs"
            songs = os.listdir(music_dir)
            print(songs)
            for i in songs:
                os.startfile(os.path.join(music_dir, i))
        
        elif "the time" in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open vs" in query:
            codePath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "run sublime" in query:
            codePath1 = "C:\\Program Files\\Sublime Text\\sublime_text.exe"
            os.startfile(codePath1)

        elif "email to tejas" in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "bhutadats@rknec.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email ")

        elif "exit" or "quit" or "close voice assistant" in query:
            speak("I hope you enjoyed the service sir!")
            speak("I hope we will meet soon")
            exit()

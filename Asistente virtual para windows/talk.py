import speech_recognition as sr
import pyttsx3, pywhatkit
import time


listener=sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
    voices = engine.getProperty("voices") 
    engine.setProperty('rate',200)
    engine.setProperty('voice', voices[4].id)
    engine.say(text)
    engine.runAndWait()
    
def speech():
    file= open("Comand.txt", "r",encoding="utf-8")
    info=file.read()
    talk(info)
    engine.endLoop()

speech()
#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pyttsx3, pywhatkit
import speech_recognition as sr
listener=sr.Recognizer()
engine = pyttsx3.init()


# In[4]:


def escucha():
   global rec
   global r
   global auxiliar
   r = sr.Recognizer()
   voice_id = 'spanish-latin-am'
   engine.setProperty('rate',190)
   with sr.Microphone() as source:
       global audio
       print("Escuchando...")
       audio = r.listen(source)
   try:
       print("dijiste: -  " + r.recognize_google(audio, language = "es-ES"))
       rec=r.recognize_google(audio, language = "es-ES")
       rec=rec.lower()
       
   except sr.UnknownValueError:
       print("No entendi lo que me dijiste!")
       rec=None
   except sr.RequestError as e:
       print("Could not request results from Google Speech Recognition service; {0}".format(e))    


# In[5]:


escucha()


# In[ ]:





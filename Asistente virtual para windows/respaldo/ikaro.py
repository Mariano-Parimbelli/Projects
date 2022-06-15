
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

#LIBRERIAS
import speech_recognition as sr
import pyttsx3, pywhatkit
import time
import pandas as pd
import spacy
import numpy as np
import re
import random
#import pyjokes
import wikipedia
import threading
import subprocess as sp
import webbrowser
import pyautogui
import os
listener=sr.Recognizer()
engine = pyttsx3.init()
nlp=spacy.load('es_core_news_lg')
from data.functions.basic_utilities import *
 
from tkinter import ttk,font
from pydub import AudioSegment 
from pydub.playback import play 


def talk(text):
    voices = engine.getProperty("voices") 
    engine.setProperty('rate',200)
    engine.setProperty('voice', voices[4].id)
    engine.say(text)
    engine.runAndWait()

def main():

    global mainWindow, z,wiki_windows


def escucha():
    def normalize(s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s
    global rec
    global r
    
    
    r = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:  
            global audio
            print("Escuchando...")
            audio = r.listen(source,phrase_time_limit=None,timeout=None)
    
   
        rec=normalize(r.recognize_google(audio, language = "es-ES"))
        print("dijiste: -  " + rec)

        global auxiliar2
        auxiliar2=("dijiste: -  " + rec)

        entry1 = ttk.Entry(width=45)
        entry1. insert(0,auxiliar2)
        entry1.configure(state="readonly")
        entry1.place(x=100, y=43)

        file = open("Dialog.txt", "w",encoding="utf-8")
        file.write(auxiliar2)
        file.close()
 
    except sr.UnknownValueError:
        play(AudioSegment.from_wav("data/sound/no_caption.wav"))
        print("No entendi lo que me dijiste!")
        rec=None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        rec = None
    except sr.WaitTimeoutError:
        rec=None
    except:
        rec=None
        pass
        

def repYoutube():
    sinonimo=re.search(r"(reproducir|pon|buscar|escuchar|ver|buscar en youtube|busca|ver en youtube|pone|quiero escuchar|)",rec)
    sinonimo=str(sinonimo.group())
    sinonimo = sinonimo.lower()
    var=0
    if sinonimo is not None:
        var=1
    else:
        var=0
    if (var==1):
        music = rec.replace(sinonimo,'')
        music = re.sub('buscar en youtube','',music)
        music = re.sub('en youtube','',music)
        music = re.sub('youtube','',music)
        music = re.sub('Reproducir','',music)
        music = re.sub('reproduci','',music)
        print("Reproduciendo..."+ music)
        talk("Reproduciendo"+ music)
        pywhatkit.playonyt(music,use_api=True)
    else :
        var=2
        talk("quizas debas decirlo de otro modo, lo siento") 


def busqGoogle():
        sinonimo=re.search(r"(buscar|busqueda|busca|goglear|google|guglia|guglea|googleen|en|)",rec)
        sinonimo=str(sinonimo.group())
        var=0
        if sinonimo is not None:
            var=1
        else:
            var=0
        if (var==1):
            busqueda=re.sub('en google','',rec)
            busqueda=re.sub(sinonimo,'',busqueda)
            busqueda=re.sub("busqueda",'',busqueda)
            busqueda=re.sub("buscar",'',busqueda)
            busqueda=re.sub("busca",'',busqueda)
            print("buscando " + busqueda)
            talk ("buscando " + busqueda)
            pywhatkit.search(busqueda) 
        else: 
            print("An unknown error occured")        


def Wikipedia():
    while True:
        sinonimo = re.search(r"(buscar|buscar definicion|busqueda|buscar|goglear|Buscar|google|guglia|guglea|dame la definicion de|la definición de|define|la definición de|definir|googleen|lds|)", rec)
        sinonimo = str(sinonimo.group())
        sinonimo = sinonimo.lower()
        var = 0
        if sinonimo is not None:
                var = 1
        else:
            var = 0
        if (var == 1):
            busqueda = rec.lower()
            busqueda = re.sub('en wikipedia', '', busqueda)
            busqueda = re.sub('de wikipedia', '', busqueda)
            busqueda = re.sub('wikipedia', '', busqueda)
            busqueda = re.sub('la definición de','',busqueda)
            busqueda = re.sub('la definicion de','',busqueda)
            busqueda = re.sub('definicion de','',busqueda)
            busqueda = re.sub('buscar la','',busqueda)
            busqueda = re.sub('buscar la definicion','',busqueda)
            busqueda = re.sub(sinonimo, '', busqueda)
            print("buscando " + busqueda)
            auxiliar2=("buscando, "  + busqueda)
            file = open("Dialog.txt", "w",encoding="utf-8")
            file.write(auxiliar2)
            file.close()
            talk("buscando ")

            wikipedia.set_lang("es")  # -----------------
                #wiki = wikipedia.page(busqueda)
            try:
                wiki = wikipedia.summary(busqueda,sentences=7)
                break
        
            except wikipedia.DisambiguationError as e:
                file = open("Dialog.txt", "w",encoding="utf-8")
                file.write("Encontre varios resultados!, ¿podrias ser mas especifico? ")
                file.close()
                print("Encontre varios resultados!")
                talk("Hay muchos resultados para " + busqueda + " ,¿podrias ser mas especifico?")
                escucha()            
            
    text=str(wiki)
    text = re.sub(r'==.*?==+', '', text)
    text = re.sub(r'\[.*?\]+', '', text)
    text = text.replace('\n', '')
    characters = ":_¡»—[];!-«©@)("
    text = ''.join(x for x in text if x not in characters)
    file = open("Comand.txt", "w",encoding="utf-8")
    file.write(text)
    file.close()
   
    def wiki_content():
        global extProc1
        time.sleep(0.5)
        extProc1 = sp.Popen(['python','wikipedia_content.py'])
   
    def ejecutar_doc1():
        global extProc
        extProc = sp.Popen(['python','talk.py'])  # ejecutas myPyScript.py 


          
    def ejecutar_doc2():
        contador=0
        time.sleep(1)
        
        while True:
            contador+=1

            print("di parar o listo si quieres detener el speak")
            escucha()
            time.sleep(0.5)
            try:
                parar = re.search(r"(parar|okey gracias|okey|gracias|entendi|entendido|para|bueno|listo|)", rec)
                parar = str(parar.group())
                if (rec == parar):
                    print("DETENIENDO...")
                    sp.Popen.terminate(extProc)
                    #sp.Popen.terminate(extProc1) # cierras el proceso
                    break
                elif (rec==None):
                    time.sleep(1)
                    continue
            except:
                print("error")
                continue
    hilo1 = threading.Thread(target=ejecutar_doc1)
    hilo2 = threading.Thread(target=wiki_content)
    hilo1.daemon=True
    hilo1.start()
    time.sleep(1)
    hilo2.start()
    ejecutar_doc2() 
     

def PagWeb():
    dic_web=pd.read_csv("dic_web.csv")
    sentence = rec
    doc = nlp(sentence)
    try:
        for e in doc.ents:
            text=str(e.text)
            text=text.lower()
            print("buscando...  " + text)

        for i in dic_web.index:
            if (dic_web["simple"][i] == text):
                link=dic_web["completa"][i]
        web="https:\\"+link
        webbrowser.open(web, new=2, autoraise=True)     
    except:
        print("No entendi a que pagina te referias podrias reformular?")


def scroll():
    
    def bajar_const():
            global extProc
            extProc = sp.Popen(['python','ScrollBajar.py'])
            extProc 
    def subir_const():
            global extProc
            extProc = sp.Popen(['python','ScrollSubir.py'])
            extProc 
    def detener():
            
            while True:
                time.sleep(0.5)
                escucha()
                try:
                    print("di parar o listo")
                    parar = re.search(r"(parar|okey gracias|okey|gracias|entendi|entendido|para|bueno|listo|)", rec)
                    parar = str(parar.group())
                    if (rec == parar):
                        print("DETENIENDO...")
                        time.sleep(0.5)
                        sp.Popen.terminate(extProc) # cierras el proceso
                        break
                        pass
                    elif (rec==None):
                        continue
                except:
                    continue
    def subir_uno():
            pyautogui.scroll(900)
    def bajar_uno():
            pyautogui.scroll(-900)
      
    while  ((rec =="bajar uno")|(rec=="baja uno")|(rec=="baja otro")|(rec=="bajar una")|(rec =="bajar otro")|(rec=="bajar otra")
           |(rec=="baja una")|(rec=="baja otra")|(rec=="anda hacia abajo")|(rec=="anda bajando")
           | (rec=="baja")|(rec=="ir bajando")|(rec=="anda hacia abajo")|(rec=="deslizar hacia abajo")
           |(rec=="subir uno")|(rec=="subir una")|(rec=="subir otro")|(rec=="subir otra")
           |(rec=="subi uno")|(rec=="subi una")|(rec=="subi otro")|(rec=="subi otra")
           |(rec=="anda subiendo")|(rec=="soy una")|(rec=="subir uno")|(rec=="deslizar hacia arriba")
           |(rec=="ir subiendo")):
            
            
        if((rec =="bajar uno")|(rec=="bajar una")|(rec =="bajar otro")|(rec=="bajar otra")
           |(rec=="baja una")|(rec=="baja otra")|(rec=="baja uno")|(rec=="baja otro")):
            bajar_uno()
            escucha()
        elif((rec=="subir uno")|(rec=="subir una")|(rec=="subir otro")|(rec=="subir otra")
           |(rec=="subi uno")|(rec=="subi una")|(rec=="subi otro")|(rec=="subi otra")
           |(rec=="soy una")|(rec=="subir uno")):
            subir_uno()
            escucha()
            
        elif ((rec=="baja")|(rec=="ir bajando")|(rec=="ir bajando")|(rec=="anda hacia abajo")
              |(rec=="deslizar hacia abajo")|(rec=="anda bajando")):
            hilo1 = threading.Thread(target=bajar_const)
            hilo2 = threading.Thread(target=detener)
            hilo1.daemon=True
            hilo1.start()
            hilo2.start()
            time.sleep(2)
           
        elif(rec == "deslizar hacia arriba")|(rec=="ir subiendo")|(rec=="anda subiendo")|(rec=="subi"):
            hilo1 = threading.Thread(target=subir_const)
            hilo2= threading.Thread(target=detener)
            hilo1.daemon=True
            hilo1.start()
            hilo2.start()
            time.sleep(2)



def correcciones(cadena):
   
    import spacy
    nlp=spacy.load('es_core_news_lg')
    from nltk.tokenize import word_tokenize
    import re
    from spacy.matcher import Matcher
    global pregunta_listata

    corregida=str(cadena)
     #===ELIMINAR STOP WORDS===
    def stopWords(corpus):
        global oraciones_filtradas
        f = open('stopwords.txt', 'r')
        stopwords = f.read().split('\n')
        f.close()
        " ".join(stopwords)
        oraciones=pd.Series(corpus)

        oraciones_filtradas = [" ".join([
                                  palabra for palabra in oracion.split()
                                  if palabra not in stopwords])
                                  for oracion in oraciones]
    stopWords(corregida)

    #===STEMMATIZAR===
    from nltk.stem import SnowballStemmer

    spanish_stemmer = SnowballStemmer('spanish')

    oraciones_filtradas_lematizadas=[]
    for oracion in oraciones_filtradas:
        oracion_lematizada = []
        for palabra in oracion.split():
            doc=nlp(palabra)
            oracion_lematizada.append(doc[0].lemma_)
        oraciones_filtradas_lematizadas.append(" ".join(oracion_lematizada))

    global pregunta_lista
    oraciones_filtradas_lematizadas_stemm=[]

    for oracion in oraciones_filtradas_lematizadas:
        oracion_stemm = []
        for palabra in oracion.split():
            oracion_stemm.append(spanish_stemmer.stem(palabra))
        oraciones_filtradas_lematizadas_stemm.append(" ".join(oracion_stemm))

    pregunta_lista=oraciones_filtradas_lematizadas_stemm



def prediccion(corpus):
    import warnings
    warnings.filterwarnings('ignore')
    import pickle
    from sklearn.feature_extraction.text import CountVectorizer
    global result
    global probabilidad
    
    loaded_vec = CountVectorizer(vocabulary=pickle.load(open("prediccion/estructure.pkl", "rb"))) 
    new_input=loaded_vec.transform(corpus)
    new_input=pd.DataFrame(new_input.toarray()) 


    clf_input=pickle.load(open("prediccion/modelo.sav", "rb"))
    probabilidad=sorted(list(clf_input.predict_proba(new_input)[0]))[-1]
    predict_input=clf_input.predict(new_input)

 
    for index,value in enumerate(predict_input):
        result=[]
        if float(probabilidad) >= 0.6:
            result.append(predict_input[index])

    
    result=np.unique(result)
    result=" ".join(result) 




def functions(result):
    if (result == "buscar_google"):
        busqGoogle()
    elif (result=="minimizar"):
        minimize()
    elif (result=="configuraciones"):
        openConfiguration()
    elif (result=="buscar_wikipedia"):
        Wikipedia()
    elif (result=="next_tab"):
        nextTab()
    elif (result=="previus_tab"):
        previusTab()
    elif (result=="close_tab"):
        closeTab()
    elif (result=="previus_pag"):
        previusPag()
    elif (result=="new_windows"):
        newWindow()
    elif (result=="abir_web"):
        PagWeb()
    elif (result=="buscar_youtube"):
        repYoutube()
    elif (result=="pausa")|(result=="play"):
        play_pause()
    elif (result=="siguiente"):
        siguiente()
    elif (result=="anterior"):
        anterior()
    elif (result=="volumenMenos"):
        volMenos()
    elif (result=="volumenMas"):
        volMas()    



if __name__ == '__main__':
 
    
    def salir():
        quit()

    while True:
        escucha()
        if (rec=="ikaro")|(rec=="icaro")|(rec=="ika")|(rec=="ica")|(rec=="escucha")|(rec=="escuchame")|(rec=="escuchar")|(rec=="picara")|(rec=="activar")|(rec=="activate"):
            play(AudioSegment.from_wav("data/sound/online.wav")) 
            while True:
                escucha()
                if (rec == None):
                    continue
                elif (rec=="adios")|(rec=="cerrar")|(rec=="chau")|(rec=="Adios")|(rec=="Chau")|(rec=="hayas"):
                    play(AudioSegment.from_wav("data/sound/exit.wav"))
                    print("Exit")
                    quit()
                
                elif (rec=="mute")|(rec=="mutear")|(rec=="deja de escuchar")|(rec=="no escuches")|(rec=="silencio")|(rec=="apagar")|(rec=="silenciar"):
                    play(AudioSegment.from_wav("data/sound/mute.wav")) 
                    break
                     
                elif(rec!=None):
                    cadena=rec 
                    correcciones(cadena)
                    prediccion(pregunta_lista)
                    print(result)
                    functions(result)
                    continue  
        elif (rec=="adios")|(rec=="cerrar")|(rec=="chau")|(rec=="Adios")|(rec=="Chau")|(rec=="hayas"):
            play(AudioSegment.from_wav("data/sound/exit.wav"))
            print("Exit")
            quit()      

        else:
            continue













    
   



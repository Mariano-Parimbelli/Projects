# Imports
from tkinter import *
import tkinter as tk
from ctypes import windll
import tkinter
from PIL import Image, ImageTk
import subprocess as sp
import threading
import pyttsx3, pywhatkit
import time
from pydub import AudioSegment 
from pydub.playback import play 

engine = pyttsx3.init()

def talk(text):
    voices = engine.getProperty("voices") 
    engine.setProperty('rate',200)
    engine.setProperty('voice', voices[4].id)
    engine.say(text)
    engine.runAndWait()

# Some WindowsOS styles, required for task bar integration
GWL_EXSTYLE = -20
WS_EX_APPWINDOW = 0x00040000
WS_EX_TOOLWINDOW = 0x00000080

lastClickX = 0
lastClickY = 0


def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y
def arrastrar(event):
    x, y = event.x - lastClickX + mainWindow.winfo_x(), event.y - lastClickY + mainWindow.winfo_y()
    mainWindow.geometry("+%s+%s" % (x , y))

def set_appwindow(mainWindow):

    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
    # re-assert the new window style
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())


def main():
    global mainWindow, z

    # Default window configuration
    mainWindow = Tk()

    def ejecutar_doc1():
        global extProc
        extProc = sp.Popen(['python','ikaro.py']) 
        
    def dialogo():
        from tkinter import ttk
        dialog=open("Dialog.txt")
        texto_dialog=dialog.read()
                 
        entry = ttk.Entry(width=50)
        entry. insert(0,texto_dialog)
        entry.configure(state="readonly")
        entry.place(x=90, y=45)
        mainWindow.after(2000,dialogo)
     

    
    def btn_hide():
        if  b1.winfo_ismapped(): 
            b1.place_forget()     
        else:
            play(AudioSegment.from_wav("data/sound/exit.wav"))
            time.sleep(1)
            sp.Popen.terminate(extProc)

            b1.place(x=400, y=27)
            b2.place_forget()
                
                

    def btn_hide2():
 
        if  b2.winfo_ismapped(): 
            b2.place_forget()            
        else:  
            b1.place_forget()
            b2.place(x=400, y=27)
            
           
            hilo1 = threading.Thread(target=ejecutar_doc1)
            hilo1.setDaemon(True)
            hilo1.start() 
            
            talk("Iniciando. Cargando condiguracion")
 
 
    
            talk("En linea")
            dialogo() 
            
            

    global b1
    global b2
    width =60
    height =60
    photo1= Image.open("resources/imagenes/icon2.png")
    photo1= photo1.resize((width, height),Image.ANTIALIAS)
    photoImg2 = ImageTk.PhotoImage(photo1)

    b1 = tk.Button(mainWindow, image = photoImg2,borderwidth = 0, command=btn_hide2)
    b1.place(x=400, y=27)
    

    width =60
    height =60
    photo= Image.open("resources/imagenes/icon.png")
    photo= photo.resize((width, height),Image.ANTIALIAS)
    photoImg = ImageTk.PhotoImage(photo)

    b2 = tk.Button(mainWindow,image = photoImg, borderwidth = 0,command=btn_hide)
    b2.place(x=400, y=27)
    b2.place_forget()
    
 

    def status_bar():
        global statusbar
        statusbar=tk.Label(mainWindow, text="Ikaro v0.0.1-- ♾️", bd=1, relief=tk.FLAT, anchor=tk.W,fg="gray", bg="black")
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        statusbar.pack(side=tk.TOP)
        mainWindow.geometry('500x90')
    status_bar()

    #CREAR FOTO
    """  photoImg = ImageTk.PhotoImage(photo)
    photo_label= Label(mainWindow, image=photoImg)
    photo_label.pack()
    """ 



    frame2 = PhotoImage(file="resources/assets/escuchando.gif", format="gif -index 2")
    bg = PhotoImage(file = "resources/imagenes/gray.gif") 
    canvas1 = Canvas( mainWindow, width =40, height =50) 
   # canvas1.pack(fill = "both", expand = True) 
    canvas1.create_image( 0, 0, image = bg,   anchor = "nw") 
    

    mainWindow.resizable(width=False, height=False)
    mainWindow.overrideredirect(True)
    mainWindow.after(10, lambda: set_appwindow(mainWindow))
    mainWindow.bind('<Button-1>', SaveLastClickPos)
    mainWindow.bind('<B1-Motion>',arrastrar)
    z = 0

 

    def exitGUI():
        salir()
        mainWindow.destroy()

    def minimizeGUI():
        global z
        mainWindow.state('withdrawn')
        mainWindow.overrideredirect(False)
        mainWindow.state('iconic')
        z = 1

    def frameMapped(event=None):
        global z
        mainWindow.overrideredirect(True)
        """mainWindow.iconbitmap("ANAL_OG.ico")
        if z == 1:
            set_appwindow(mainWindow)
            z = 0"""

    close_button = Button(statusbar, text='✘', command=exitGUI, width=5, bg="#090909", fg="#888", bd=0)
    close_button.pack(side=tk.RIGHT)

    btn_minimize = tk.Button(statusbar, text="▬", command=minimizeGUI, width=5, bg="#090909", fg="#888", bd=0)
    btn_minimize.pack(side=tk.RIGHT)

 
    mainWindow.bind("<Map>", frameMapped)  # This brings back the window
    mainWindow.mainloop()  # Window Loop


    
if __name__ == '__main__':
    def salir():
        quit()
    main()
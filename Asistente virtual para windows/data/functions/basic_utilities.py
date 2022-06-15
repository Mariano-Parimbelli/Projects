#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pyautogui
import time


#  ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',                   
# ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',                         
# '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',                        
# 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',               
# 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',          
# 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',               
# 'browserback', 'browserfavorites', 'browserforward', 'browserhome',                  
# 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',                   
# 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',               
# 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',                  
# 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',               
# 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',               
# 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',               
# 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',                 
# 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',                    
# 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',                
# 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',                      
# 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',             
# 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',             
# 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',                 
# 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'w                              

# In[ ]:



    


# In[4]:

def nextTab():
     pyautogui.hotkey("ctrlright","pagedown")
def previusTab():
    pyautogui.hotkey("ctrlright","pageup")
def newTab():
     pyautogui.keyUp('shift')  
     pyautogui.hotkey('ctrl', 't')
def newWindow():
     pyautogui.keyUp('shift')  
     pyautogui.hotkey('ctrl', 'n')
def closeTab():
    try:
        pyautogui.keyUp('shift')  
        pyautogui.hotkey('ctrl', 'w')
    except:
        pyautogui.keyUp('shift')  
        pyautogui.hotkey('ctrl', 'f4')
def minimize():
    pyautogui.keyDown('alt')  
    pyautogui.keyDown('space')
    pyautogui.keyDown('n')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('space')
    pyautogui.keyUp('n')
def minimizeAll():
     pyautogui.keyUp('shift')  
     pyautogui.hotkey('win', 'm')
def closeWindowActual():
    pyautogui.keyDown('alt')  
    pyautogui.keyDown('f4')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('f4')
def openExplorerFiles():
    pyautogui.keyUp('shift')  
    pyautogui.hotkey('win', 'e')
def openConfiguration():
    pyautogui.keyUp('shift')  
    pyautogui.hotkey('win', 'i')
def lockSession():
    pyautogui.keyUp('shift')  
    pyautogui.hotkey('win', 'l')
def previusPag(): 
    pyautogui.hotkey("alt","left")
def play_pause():
     pyautogui.hotkey("playpause")
def siguiente():
     pyautogui.hotkey("nexttrack")
def anterior():
     pyautogui.hotkey("prevtrack")
def volMas():
    pyautogui.hotkey("volumeup")
    pyautogui.hotkey("volumeup")
    pyautogui.hotkey("volumeup")
    pyautogui.hotkey("volumeup")
    pyautogui.hotkey("volumeup")
def volMenos():
    pyautogui.hotkey("volumedown")
    pyautogui.hotkey("volumedown")
    pyautogui.hotkey("volumedown")
    pyautogui.hotkey("volumedown")
    pyautogui.hotkey("volumedown")
def mute():
    pyautogui.hotkey("volumemute")
   
    
# In[3]:





# In[7]:





# In[13]:



 


# In[3]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[3]:



import pyautogui


# In[4]:


def bajar_const():
    for i in range(400):
        pyautogui.scroll(-10)      
def subir_const():               
    for i in range(400):
        pyautogui.scroll(10)
        
def bajar_1():
    pyautogui.scroll(-400)
def subir_1():
    pyautogui.scroll(400)    
def detener():
    pyautogui.scroll(0)  


# In[5]:





# In[ ]:





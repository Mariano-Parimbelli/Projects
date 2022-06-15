 
 
 
from tkinter import ttk,font


dialog=open("Comand.txt",encoding="utf8")
texto_dialog=dialog.read()               

import tkinter as tk
  
  
window = tk.Tk()
window.geometry("350x350")

window.title("Wiki Content -(CTRL+C) COPY")
window.resizable(width=False, height=False)
text = tk.Text(window, height=19, width=40)
scroll = tk.Scrollbar(window)
text.configure(yscrollcommand=scroll.set)
text.pack(side=tk.LEFT)
  
scroll.config(command=text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
  
text.insert(tk.END,texto_dialog)
text.configure(state='disabled')
tk.mainloop()
 

 
 
from datetime import time
from tkinter import*
from tkinter.ttk import*

from time import strftime

Root = Tk()
Root.title("Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text = string)
    label.after(1000, time)

label = Label(Root, font=("ds-digital", 60), background = 'black', foreground = 'cyan')
label.pack(anchor='center')

time()
mainloop()

# !/usr/bin/python3                                                                                                  
import tkinter as tk
from tkinter import *
from tkinter import messagebox

top = Tk()

#Title of  "container"
top.title("Jorge\'s GUI")


def helloCallBack():
                           #Box title,      Message
    messagebox.showinfo( "Hello Python", "Hello World")
    
    
myButton    = tk.Button(top,      text ="Hello",   command = helloCallBack)


CheckVar1 = IntVar()
CheckVar2 = IntVar()

checkSelect = IntVar()
checkSelect.set(0)

def testSelect():
    if checkSelect.get() == 0:
        labelText = Label(text="It worked").pack()
        messagebox.showinfo( "Hello Python", "Hello Wordfssfsfsdfld")
    else:
        labelText = Label(text="Please select an item from the checklist below").pack()
        messagebox.showinfo( "Hellod")

#CheckBox 1 and 2
C1 = Checkbutton(top, text = "Music", variable=checkSelect, onvalue = 1, offvalue = 0, height = 5, width = 20)
C2 = Checkbutton(top, text = "Video", variable = testSelect, onvalue = 1, offvalue = 0, height = 5, width = 20)
myButton2    = tk.Button(top,      text ="Hello",   command = testSelect)



#Loads to tk    
myButton.pack()
myButton2.pack()
C1.pack()
C2.pack()
    
# Code to add widgets will go here...
top.mainloop()
    

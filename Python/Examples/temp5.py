#We need to the interpreter wich version to use.
#Otherwise, we will have to test try, except tk VS Tk
'''
#!/usr/local/bin/python3
'''


#########PYTHON2==========


#from tkinter import *
import tkMessageBox
from Tkinter import * #V2 Syntax                                                   
import Tkinter as Tkinter
#=============--Imports ENDS--=================                                        

top = Tkinter.Tk()
top.title("Jorge\'s GUI")


def helloCallBack():
    #-------------------->    Box title,      Message
    tkMessageBox.showinfo( "Hello Python", "Hello World")

#Button_Var = Onject.Method(Object,   Button_Tittle,   Parameter<a function in this case> )
myButton    = Tkinter.Button(top,      text ="Hello",   command = helloCallBack)


myButton.pack()
top.mainloop()

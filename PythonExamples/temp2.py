
from tkinter import *
#import tkMessageBox

mGui = Tk()
top = Tk()

checkCmd = IntVar()
checkCmd.set(0)
def runSelectedItems():
    if checkCmd.get() == 0:
        labelText = Label(text="It worked").pack()
    else:
        labelText = Label(text="Please select an item from the checklist below").pack()
        
        checkBox1 = Checkbutton(mGui, variable=checkCmd, onvalue=1, offvalue=0, text="Command  Prompt").pack()
        buttonCmd = Button(mGui, text="Run Checked Items", command=runSelectedItems).pack()    
        
        
checkBox1 = Checkbutton(top, variable=checkCmd, onvalue=1, offvalue=0, text="Command  Prompt")

checkBox1.pack()
# Code to add widgets will go here...
top.mainloop()


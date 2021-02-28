import sys

from tkinter import *
from tkinter import filedialog

from subprocess import Popen

#Info
version='ALPHA2'
'''CONTRIBUTORS:
-Vhou-Atroph'''

#Window
global window
window=Tk()
window.title("Discord.py Bot Panel")

#Bot Stuff
global botfile
global bottoken
botfile=str()
bottoken=str()

#File Selection - Basics
fileselect=Frame(window)
pyfilebtn=Button(fileselect,text="Select File")
pyfilelbl=Label(fileselect,text="File: "+botfile)

#File Selection - Function
def findFile():
  global botfile0
  botfile0=filedialog.askopenfilename(initialdir="/",
  title="Select a File",
  filetypes=((".py files","*.py*"),
  ("All files","*.*")))

  pyfilelbl.configure(text="File: "+botfile0)

pyfilebtn.configure(command=findFile)

#File Selection - Display
pyfilebtn.pack(side=TOP)
pyfilelbl.pack(side=LEFT,padx=10,pady=5)

#Run Bot - Basics
run=Frame(window)
runbotbtn=Button(run,text="Run Bot")

#Run Bot - Function
def runbot():
  global botRunning
  botRunning=Popen(["python",botfile0])
  runbotbtn.configure(command=stopbot,text="Stop Bot")
def stopbot():
  botRunning.kill()
  print("Bot stopped.")
  runbotbtn.configure(command=runbot,text="Run Bot")

runbotbtn.configure(command=runbot)

#Run Bot - Display
runbotbtn.pack()

#Frames - Display
fileselect.pack(side=TOP)
run.pack(side=BOTTOM,pady=2)

window.mainloop()
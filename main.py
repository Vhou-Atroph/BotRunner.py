import sys
from tkinter import *
from tkinter import filedialog
from subprocess import Popen

#Info
'''
VERSION: 1.0.0

CONTRIBUTORS:
-Vhou-Atroph
'''

#Window
global window
window=Tk()
window.title("Discord.py Bot Panel")
window.geometry('175x100')
window.resizable(0,0)

#File Selection - Basics
fileselect=Frame(window)
pyfilebtn=Button(fileselect,text="Select File")
pyfilelbl=Label(fileselect,text="File: ")

#File Selection - Function
def findFile():
  global botfile
  botfile=filedialog.askopenfilename(initialdir="/",
  title="Select a File",
  filetypes=(("Python files","*.py*"),
  ("All files","*.*")))
  pyfilelbl.configure(text="File: "+botfile)

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
  botRunning=Popen(["python",botfile])
  runbotbtn.configure(command=stopbot,text="Stop Bot",fg='red')
def stopbot():
  botRunning.kill()
  print("Bot stopped.")
  runbotbtn.configure(command=runbot,text="Run Bot",fg='green')

runbotbtn.configure(command=runbot,fg='green')

#Run Bot - Display
runbotbtn.pack()

#Frames - Display
fileselect.pack(pady=2)
run.pack(pady=2)

window.mainloop()
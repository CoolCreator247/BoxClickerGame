# Import Modules
from tkinter import *
import random
import time

# create root window
root = Tk()

# def functions
def RunCode1():
    bg = "black"
    time.sleep(2)
    bg = "blue"
    time.sleep(2)
    bg = "black"
  
def RunCode2():
    bg = "black"
    time.sleep(2)
    bg = "green"
    time.sleep(2)
    bg = "black"

def RunCode3():
    bg = "black"
    time.sleep(2)
    bg = "white"
    time.sleep(2)
    bg = "black"
  
def RunCode4():
    bg = "black"
    time.sleep(2)
    bg = "yelow"
    time.sleep(2)
    bg = "black"

  
def RunCode():
    list1 = [1, 2, 3, 4]
    for x in range (1,4):
        TheRandomChoice = random.choice(list1)
        if TheRandomChoice == 1:
            frame = Frame(root)
            frame.pack()
            bottomframe = Frame(root)
            bottomframe.pack( side = BOTTOM )
            redbutton = Button(frame, text = '1', fg = "black",                      command=RunCode1)   
            redbutton.pack( side = LEFT)           

        if TheRandomChoice == 2:
          frame = Frame(root)
          frame.pack()
          bottomframe = Frame(root)
          bottomframe.pack( side = BOTTOM )
          greenbutton = Button(frame, text = '2', fg = "black",            command=RunCode2)
          greenbutton.pack( side = LEFT )

        if TheRandomChoice == 3:
          frame = Frame(root)
          frame.pack()
          bottomframe = Frame(root)
          bottomframe.pack( side = BOTTOM )
          bluebutton = Button(frame, text ='3', fg = "black", command=RunCode3)
bluebutton.pack( side = LEFT )

        if TheRandomChoice == 4:
          frame = Frame(root)
          frame.pack()
          bottomframe = Frame(root)
          bottomframe.pack( side = BOTTOM )
            blackbutton = Button(bottomframe, text ='4', fg ='black', command=RunCode4)
blackbutton.pack( side = BOTTOM)

            
                                   
# root window title and dimension
root.title("Box Clicker")

root.geometry('350x200')

# button widget with red color text
# inside
btn = Button(root, text="Click to start",
             fg="black", command=RunCode)
# set Button grid
btn.grid(column=1, row=0)

root.mainloop()


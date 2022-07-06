# Import Modules
from tkinter import *
import random
import time

# create root window
root = Tk()

def RunCode():
    list1 = [1, 2, 3, 4]
    for x in range (1,4):
        TheRandomChoice = random.choice(list1)
        if TheRandomChoice == 1:
            def RunCode1():
                bg = "black"
                time.sleep(2)
                bg = "blue"
                time.sleep(2)
                bg = "black"
        if TheRandomChoice == 2:
            def RunCode2():
                bg = "black"
                time.sleep(2)
                bg = "green"
                time.sleep(2)
                bg = "black" 
        if TheRandomChoice == 3:
            def RunCode3():
                bg = "black"
                time.sleep(2)
                bg = "red"
                time.sleep(2)
                bg = "black"
        if TheRandomChoice == 4:
            def RunCode4():
                bg = "black"
                time.sleep(2)
                bg = "yelow"
                time.sleep(2)
                bg = "black"                       

    btn = Button(root, text="1",
                  command=RunCode1)
    btn = Button(root, text="2",
                 fg="black", command=RunCode2)
    btn = Button(root, text="3",
                 fg="black", command=RunCode3)
    btn = Button(root, text="4",
                 fg="black", command=RunCode4)
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

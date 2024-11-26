from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title("Digital Clock")


digi_clock = Label(root, font=("arial", 150), bg="gray",fg="black")
digi_clock.pack()


root.mainloop()
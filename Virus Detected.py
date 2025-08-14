from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.askretrycancel("Choose","Do You Want To Retry?")

button = Button(root, text= "Retry", command=msg)
button.place(x=40, y=80)

root.mainloop()
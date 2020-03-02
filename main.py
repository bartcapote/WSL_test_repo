from tkinter import *


root = Tk()

def myClick():
    myLabel = Label(root, text="Look! It clicked!")
    myLabel.pack()


myButton = Button(root, text="Clickerino? :->", pad=50)
myButton.pack()


root.mainloop()
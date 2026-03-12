# Color chooser example = opens a dialog that lets the user select a color

from tkinter import *  # import tkinter GUI components
from tkinter import colorchooser  # import the color chooser module

def click():  # function runs when the button is clicked
    color = colorchooser.askcolor()  # open color picker dialog and store result

    # askcolor() returns a tuple: ((R,G,B), "#hexcode")
    colorHex = color[1]  # get the hexadecimal color value (e.g., #ff0000)

    window.config(bg=colorHex)  # change the window background to the selected color

window = Tk()  # create the main application window
window.geometry("420x420")  # set window size

# button that opens the color chooser
button = Button(window,text='Click Me',command=click)
button.pack()

window.mainloop()  # start the tkinter event loop
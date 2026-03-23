# Key event example = detects keyboard input and responds to key presses

from tkinter import *  # import tkinter GUI components

def doSomething(event):  # function runs whenever a key is pressed
    # event.keysym gives the name of the key pressed (e.g., 'a', 'Enter', 'Shift')
    # print("You pressed: " + event.keysym)
    label.config(text=event.keysym)  # update label to display the pressed key

window = Tk()  # create the main window
window.title("Key Event Example")

# bind all key press events to the function
window.bind("<Key>", doSomething)

# label to display the key pressed
label = Label(
    window,
    font=("Helvetica",100)  # large font for visibility
)
label.pack()

window.mainloop()  # start the tkinter event loop
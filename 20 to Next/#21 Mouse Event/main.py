# Mouse event example = detects mouse actions like clicks, movement, etc.

from tkinter import *  # import tkinter GUI components

def doSomething(event):  # function runs when a mouse event occurs
    # event.x and event.y give the mouse position inside the window
    print("Mouse coordinates: " + str(event.x) + "," + str(event.y))

window = Tk()  # create the main application window
window.title("Mouse Event Example")

# bind left mouse click to the function
window.bind("<Button-1>", doSomething)  # left click

# other useful mouse events (uncomment to test)
# window.bind("<Button-2>", doSomething)  # middle click (scroll wheel)
# window.bind("<Button-3>", doSomething)  # right click
# window.bind("<ButtonRelease>", doSomething)  # when mouse button is released
# window.bind("<Enter>", doSomething)  # when mouse enters the window
# window.bind("<Leave>", doSomething)  # when mouse leaves the window
# window.bind("<Motion>", doSomething)  # when mouse moves inside the window

window.mainloop()  # start the tkinter event loop

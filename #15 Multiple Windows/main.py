# creating multiple windows in tkinter

from tkinter import *

def create_window():
    # Toplevel() creates a new window linked to the main (parent) window
    new_window = Toplevel(old_window)

    # Tk() would create a completely separate independent window (not recommended multiple times)
    # new_window = Tk()

    # add something inside the new window so it's not empty
    Label(new_window, text="This is a new window").pack()

    # old_window.destroy()  # uncomment this if you want to close the main window

old_window = Tk()  # create the main window

# button that creates a new window when clicked
Button(
    old_window,
    text="Create New Window",
    command=create_window
).pack()

old_window.mainloop()  # start the GUI event loop
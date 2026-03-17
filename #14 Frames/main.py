# frame = a rectangular container used to group and organize other widgets

from tkinter import *  # import tkinter GUI components

window = Tk()  # create the main window

# create a frame inside the window
frame = Frame(
    window,        # parent window
    bg="pink",     # background color of the frame
    bd=5,          # border thickness
    relief=SUNKEN  # border style (gives a sunken/3D look)
)

frame.pack()  # add the frame to the window

# create buttons inside the frame (like WASD controls)

Button(
    frame,                 # place button inside the frame
    text="W",              # text on button
    font=("Consolas",25),  # font style and size
    width=3                # width of button
).pack(side=TOP)           # position at the top of the frame

Button(
    frame,
    text="A",
    font=("Consolas",25),
    width=3
).pack(side=LEFT)          # position to the left

Button(
    frame,
    text="S",
    font=("Consolas",25),
    width=3
).pack(side=LEFT)          # position next to A (left side)

Button(
    frame,
    text="D",
    font=("Consolas",25),
    width=3
).pack(side=LEFT)          # position next to S (left side)

window.mainloop()
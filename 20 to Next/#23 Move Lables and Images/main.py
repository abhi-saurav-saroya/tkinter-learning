# ------------ move widgets using Label (place) ------------

from tkinter import *  # import tkinter GUI components

def move_up(event):    # move label up
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)

def move_down(event):  # move label down
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)

def move_left(event):  # move label left
    label.place(x=label.winfo_x() - 10, y=label.winfo_y())

def move_right(event): # move label right
    label.place(x=label.winfo_x() + 10, y=label.winfo_y())

window = Tk()  # create main window
window.geometry("500x500")

# bind keyboard keys (WASD + arrow keys) to movement functions
window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

# load image and place it inside a label
myimage = PhotoImage(file='racecar.png')
label = Label(window, image=myimage)
label.place(x=0, y=0)  # initial position

window.mainloop()  # run first window


# ------------ move image inside Canvas ------------

from tkinter import *

def move_up(event):    # move image up
    canvas.move(myimage, 0, -10)

def move_down(event):  # move image down
    canvas.move(myimage, 0, 10)

def move_left(event):  # move image left
    canvas.move(myimage, -10, 0)

def move_right(event): # move image right
    canvas.move(myimage, 10, 0)

window = Tk()  # create new window

# bind movement keys (WASD)
window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

# create canvas (drawing area)
canvas = Canvas(window, width=500, height=500)
canvas.pack()

# load image and place it on the canvas
photoimage = PhotoImage(file='racecar.png')
myimage = canvas.create_image(0, 0, image=photoimage, anchor=NW)

window.mainloop()  # run secondaaaaaaaaaaaad window
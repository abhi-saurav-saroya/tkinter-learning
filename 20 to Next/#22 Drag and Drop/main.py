# Drag and drop example = allows widgets to be moved with the mouse

from tkinter import *

def drag_start(event):  # runs when mouse button is pressed on the widget
    widget = event.widget  # get the widget that triggered the event
    widget.startX = event.x  # store initial mouse X position inside the widget
    widget.startY = event.y  # store initial mouse Y position inside the widget

def drag_motion(event):  # runs when the mouse is moved while holding the button
    widget = event.widget  # get the widget being dragged
    # calculate new position of the widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y

    widget.place(x=x, y=y)  # move the widget to the new position

window = Tk()  # create the main window
window.title("Drag and Drop Example")

# create first draggable label
label = Label(window, bg="red", width=10, height=5)
label.place(x=0, y=0)  # place it at initial position

# create second draggable label
label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=100, y=100)

# bind mouse events to the first label
label.bind("<Button-1>", drag_start)   # when mouse button is pressed
label.bind("<B1-Motion>", drag_motion) # when mouse is dragged

# bind mouse events to the second label
label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)

window.mainloop()  # start the tkinter event loop
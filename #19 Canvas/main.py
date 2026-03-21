# Canvas = widget used to draw shapes, lines, arcs, images, etc.

from tkinter import *  # import tkinter GUI components

window = Tk()  # create the main window
window.title("Canvas Example")

# create a canvas (drawing area)
canvas = Canvas(
    window,
    height=500,  # height of canvas
    width=500    # width of canvas
)

# examples of drawing (currently commented)

# canvas.create_line(0,0,500,500,fill="blue",width=5)  # diagonal line
# canvas.create_line(0,500,500,0,fill="red",width=5)   # opposite diagonal

# canvas.create_rectangle(50,50,250,250,fill="purple")  # rectangle

# points = [250,0,500,500,0,500]
# canvas.create_polygon(points,fill="yellow",outline="black",width=5)  # triangle

# canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5)  # arc slice

# draw a red semicircle (top half)
canvas.create_arc(
    0, 0, 500, 500,  # bounding box coordinates
    fill="red",
    extent=180,      # angle of arc (half circle)
    width=10
)

# draw a white semicircle (bottom half)
canvas.create_arc(
    0, 0, 500, 500,
    fill="white",
    extent=180,
    start=180,       # start angle for bottom half
    width=10
)

# draw a small white circle in the center
canvas.create_oval(
    190, 190, 310, 310,  # coordinates of the oval
    fill="white",
    width=10
)

canvas.pack()  # add canvas to window

window.mainloop()  # start the tkinter event loop
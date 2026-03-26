# Animation example = moving an image (UFO) that bounces off window edges

from tkinter import *  # import tkinter GUI components
import time  # used to control animation speed

# window dimensions
WIDTH = 500
HEIGHT = 500

# initial movement speed (velocity)
xVelocity = 3
yVelocity = 2

window = Tk()  # create main window
window.title("Bouncing UFO")

# create canvas (drawing area)
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# load and display background image
background_photo = PhotoImage(file='space.png')
background = canvas.create_image(0, 0, image=background_photo, anchor=NW)

# load and display moving object (UFO)
photo_image = PhotoImage(file='ufo.png')
my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)

# get dimensions of the image (used for boundary detection)
image_width = photo_image.width()
image_height = photo_image.height()

# infinite loop for animation
while True:
    coordinates = canvas.coords(my_image)  # get current (x, y) position of image
    # print(coordinates)  # debug: prints position

    # check collision with left/right walls
    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        xVelocity = -xVelocity  # reverse horizontal direction

    # check collision with top/bottom walls
    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        yVelocity = -yVelocity  # reverse vertical direction

    canvas.move(my_image, xVelocity, yVelocity)  # move image

    window.update()  # update the window manually (since we're using a loop)
    time.sleep(0.01)  # small delay to control speed of animation

window.mainloop()  # (technically not reached due to infinite loop)
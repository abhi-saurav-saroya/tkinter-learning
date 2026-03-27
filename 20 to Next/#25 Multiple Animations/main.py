# Bouncing balls animation using a custom Ball class

from tkinter import *  # import tkinter GUI components
import time  # used to control animation speed


# Ball class = defines how each ball behaves
class Ball:

    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas  # store reference to canvas

        # create a circle (oval) on the canvas
        self.image = canvas.create_oval(
            x, y, x + diameter, y + diameter, fill=color
        )

        # store velocity values
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):  # method to move the ball
        coordinates = self.canvas.coords(self.image)  # get current position

        # check collision with left/right walls
        if coordinates[2] >= self.canvas.winfo_width() or coordinates[0] < 0:
            self.xVelocity = -self.xVelocity  # reverse horizontal direction

        # check collision with top/bottom walls
        if coordinates[3] >= self.canvas.winfo_height() or coordinates[1] < 0:
            self.yVelocity = -self.yVelocity  # reverse vertical direction

        # move the ball by its velocity
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)


# create main window
window = Tk()
window.title("Bouncing Balls")

WIDTH = 500
HEIGHT = 500

# create canvas (drawing area)
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# create multiple Ball objects with different sizes and speeds
volley_ball = Ball(canvas, 0, 0, 100, 1, 1, "white")
tennis_ball = Ball(canvas, 0, 0, 50, 4, 3, "yellow")
basket_ball = Ball(canvas, 0, 0, 125, 3, 5, "orange")
bowling_ball = Ball(canvas, 0, 0, 75, 2, 1, "black")

# animation loop
while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    bowling_ball.move()

    window.update()   # manually refresh the window
    time.sleep(0.01)  # control animation speed

window.mainloop()  # (not reached due to infinite loop)
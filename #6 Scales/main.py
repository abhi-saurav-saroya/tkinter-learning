# Scale widget example = a slider that lets the user choose a numeric value

from tkinter import *

def submit():
    # scale.get() returns the current value selected on the slider
    print("The temperature is: " + str(scale.get()) + " degrees C")

window = Tk()

hotImage = PhotoImage(file='hot.png') # load the image representing "hot"
hotLabel = Label(window, image=hotImage) # create a label to display the hot image
hotLabel.pack()  # place it at the top of the window

# create the Scale widget (a vertical slider)
scale = Scale(
    window,                 # parent window where the widget appears
    from_=100,              # maximum value at the top
    to=0,                   # minimum value at the bottom (reversed scale)
    length=400,             # total height of the slider in pixels
    orient=VERTICAL,        # slider orientation (VERTICAL or HORIZONTAL)
    font=('Consolas',20),   # font used for the numeric tick labels
    tickinterval=10,        # show tick marks every 10 units
    # showvalue=0,          # uncomment to hide the current value display
    resolution=5,           # slider moves in steps of 5
    troughcolor='#69EAFF',  # color of the slider track
    fg='#FF1C00',           # color of the tick numbers
    bg='#111111'            # background color of the scale widget
)

# set the slider's starting position to the middle value
scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])
scale.pack()  # add the slider to the window

coldImage = PhotoImage(file='cold.png') # load the image representing "cold"
coldLabel = Label(window, image=coldImage) # create a label to display the cold image
coldLabel.pack()  # place it below the slider

# create a button that prints the selected temperature
button = Button(window, text='submit', command=submit)
button.pack()  # add the button to the window

window.mainloop()  # start the tkinter event loop (keeps the window running)
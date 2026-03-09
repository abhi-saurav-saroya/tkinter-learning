# Radiobutton example = similar to checkboxes, but only ONE option can be selected from the group

from tkinter import *  # import all Tkinter GUI components

# list of food options
food = ["Chole Bhature", "Samosa", "Biryani"]

def order():  # function that runs whenever a radiobutton is selected
    if x.get() == 0:  # first radiobutton selected
        print("You ordered Chole Bhature!")
    elif x.get() == 1:  # second radiobutton selected
        print("You ordered Samosa!")
    elif x.get() == 2:  # third radiobutton selected
        print("You ordered Biryani!")
    else:  # fallback (should normally never happen)
        print("huh?")

window = Tk()  # create the main application window

# load images for each food item
choleImage = PhotoImage(file='chole_bhature.png').zoom(2, 2)
samosaImage = PhotoImage(file='samose.png').zoom(2, 2)
biryaniImage = PhotoImage(file='biryani.png').zoom(2, 2)

# store images inside a list so we can access them easily using index
foodImages = [choleImage, samosaImage, biryaniImage]

x = IntVar()  # variable shared by all radiobuttons (stores selected option)

# loop through the food list and create radiobuttons dynamically
for index in range(len(food)):
    radiobutton = Radiobutton(
        window,                     # parent window
        text=food[index],           # text displayed next to the radiobutton
        variable=x,                 # groups radiobuttons together (same variable)
        value=index,                # unique value assigned to each radiobutton
        padx=25,                    # horizontal padding inside the widget
        font=("Impact", 40),        # font style and size
        image=foodImages[index],    # image displayed with the radiobutton
        compound='left',            # place image to the left of text
        # indicatoron=0,            # removes the circle indicator if uncommented
        # width=375,                # sets fixed width for the button
        command=order               # function executed when button is selected
    )
    radiobutton.pack(anchor=W)      # place the radiobutton aligned to the left, w = west

window.mainloop()  # start the Tkinter event loop
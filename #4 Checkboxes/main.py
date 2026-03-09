# Checkbutton example: user can select Python, C++, both, or none

from tkinter import *

def display():  # function that runs whenever a checkbox is clicked
    if x.get() == 1 and y.get() == 0:
        print("I like Python")
    elif x.get() == 0 and y.get() == 1:
        print("I like C++")
    elif x.get() == 1 and y.get() == 1:
        print("I like both Python & C++")
    else:
        print("I don't like either")

window = Tk()  # create the main application window

# IntVar variables store the state of the checkboxes (0 = unchecked, 1 = checked)
x = IntVar()
y = IntVar()

# load images and shrink them using subsample so they fit inside the checkbox nicely
python_img = PhotoImage(file="python_logo.png").subsample(4,4)
cpp_img = PhotoImage(file="cpp_logo.png").subsample(4,4)

# create the Python checkbox widget
checkbox = Checkbutton(
    window,                 # parent window where the widget will appear
    text="Python",          # text displayed next to the checkbox
    variable=x,             # variable that tracks the checkbox state
    onvalue=1,              # value stored when checkbox is checked
    offvalue=0,             # value stored when checkbox is unchecked
    command=display,        # function that runs when checkbox state changes
    font=("Arial",20),      # font style and size for the text
    fg="#00FF00",           # text color
    bg="#000000",           # background color of the checkbox
    activeforeground="#0000FF",  # text color when clicked
    activebackground="#000000",  # background color when clicked
    image=python_img,       # image displayed with the checkbox
    compound="left",        # place the image to the left of the text
    padx=25,                # horizontal padding inside the widget
    pady=10,                # vertical padding inside the widget
    width=250,              # width of the checkbox area
    height=50,              # height of the checkbox area
    anchor="w"              # align content to the left side (west)
)
checkbox.pack()  # place the checkbox in the window using pack layout

# create the C++ checkbox widget
checkbox2 = Checkbutton(
    window,
    text="C++",             # text displayed next to the checkbox
    variable=y,             # variable tracking this checkbox state
    onvalue=1,
    offvalue=0,
    command=display,        # same function handles both checkboxes
    font=("Arial",20),
    fg="#0000FF",           # text color
    bg="#000000",           # background color
    activeforeground="#0000FF",
    activebackground="#000000",
    image=cpp_img,          # C++ logo image
    compound="left",        # place image to the left of text
    padx=25,
    pady=10,
    width=250,
    height=50,
    anchor="w"              # left alignment
)
checkbox2.pack()  # add the checkbox to the window

window.mainloop()  # start the Tkinter event loop (keeps the window running)
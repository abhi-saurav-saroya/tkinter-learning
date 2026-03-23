# Text widget = works like a text area where the user can type multiple lines

from tkinter import *

def submit():  # function runs when the submit button is clicked
    input = text.get("1.0", END)  # get text from the widget (from line 1, char 0 to the end)
    print(input)  # print the entered text to the console

window = Tk()

# create the Text widget
text = Text(
    window,
    bg="light yellow",        # background color of the text area
    font=("Ink Free",25),     # font style and size
    height=8,                 # number of visible text rows
    width=20,                 # width measured in characters
    padx=20,                  # internal horizontal padding
    pady=20,                  # internal vertical padding
    fg="purple"               # text color
)

text.pack()  # add the text widget to the window

# button that retrieves the text from the Text widget
button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()  # start the tkinter event loop
# grid() = geometry manager that arranges widgets in a table-like structure (rows & columns)

from tkinter import *

window = Tk()  # create the main window

# title label spanning across 2 columns
titleLabel = Label(
    window,
    text="Enter your info",
    font=("Arial",25)
)
titleLabel.grid(row=0, column=0, columnspan=2)  # span across both columns

# first name label and entry
firstNameLabel = Label(
    window,
    text="First name: ",
    width=20,
    bg="red"
)
firstNameLabel.grid(row=1, column=0)  # row 1, column 0

firstNameEntry = Entry(window)
firstNameEntry.grid(row=1, column=1)  # row 1, column 1

# last name label and entry
lastNameLabel = Label(
    window,
    text="Last name: ",
    bg="green"
)
lastNameLabel.grid(row=2, column=0)

lastNameEntry = Entry(window)
lastNameEntry.grid(row=2, column=1)

# email label and entry
emailLabel = Label(
    window,
    text="Email: ",
    bg="blue"
)
emailLabel.grid(row=3, column=0)

emailEntry = Entry(window)
emailEntry.grid(row=3, column=1)

# submit button spanning across both columns
submitButton = Button(
    window,
    text="Submit"
)
submitButton.grid(row=4, column=0, columnspan=2)

window.mainloop()  # start the tkinter event loop
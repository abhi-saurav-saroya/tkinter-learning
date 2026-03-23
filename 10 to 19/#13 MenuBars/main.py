# Menu widget example = creates a simple menu bar with File and Edit options

from tkinter import *  # import tkinter GUI components

# functions that run when menu items are clicked
def openFile():
    print("File has been opened!")

def saveFile():
    print("File has been saved!")

def cut():
    print("You cut some text!")

def copy():
    print("You copied some text!")

def paste():
    print("You pasted some text!")


window = Tk()

# create the menu bar
menubar = Menu(window)

# attach the menu bar to the window
window.config(menu=menubar)

# create the "File" menu
fileMenu = Menu(menubar, tearoff=0, font=("MV Boli",15))  # tearoff=0 removes dashed line
menubar.add_cascade(label="File", menu=fileMenu)  # add File menu to the menu bar

# add commands inside the File menu
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()  # adds a separator line
fileMenu.add_command(label="Exit", command=quit)

# create the "Edit" menu
editMenu = Menu(menubar, tearoff=0, font=("MV Boli",15))
menubar.add_cascade(label="Edit", menu=editMenu)  # add Edit menu to the menu bar

# add commands inside the Edit menu
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()  # start the GUI event loop
# Listbox = a widget that displays a list of selectable text items inside its own container

from tkinter import *

def submit():  # function runs when the submit button is clicked
    food = []  # list that will store selected food items

    for index in listbox.curselection():     # curselection() returns a tuple of selected item indexes
        food.insert(index, listbox.get(index))  # get the text at that index and store it

    print("You have ordered: ")
    for item in food:  # print all selected items
        print(item)

def add():  # function to add a new item from the entry box to the listbox
    listbox.insert(listbox.size(), entryBox.get())  # .get() gets the entry from entry widget and then .insert() inserts item at the end of the list
    listbox.config(height=listbox.size())  # adjust listbox height to fit items

def delete():  # function to delete selected items from the listbox
    # reversed() is used so deleting items doesn't change the remaining indexes
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())  # update listbox height after deletion

window = Tk()  # create the main application window

# create the listbox widget
listbox = Listbox(
    window,
    bg="#f7ffde",           # background color
    font=("Constantia",35), # font style and size
    width=12,               # width measured in characters
    selectmode=MULTIPLE     # allows multiple items to be selected
)
listbox.pack()  # place the listbox in the window

# insert default items into the listbox
listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())  # adjust height to match number of items

# entry box where user can type a new food item
entryBox = Entry(window)
entryBox.pack()

# frame used to organize buttons neatly in one row
frame = Frame(window)
frame.pack()

# button to submit selected items
submitButton = Button(frame, text="submit", command=submit)
submitButton.pack(side=LEFT)

# button to add new item from entry box
addButton = Button(frame, text="add", command=add)
addButton.pack(side=LEFT)

# button to delete selected items
deleteButton = Button(frame, text="delete", command=delete)
deleteButton.pack(side=LEFT)

window.mainloop()  # start the tkinter event loop
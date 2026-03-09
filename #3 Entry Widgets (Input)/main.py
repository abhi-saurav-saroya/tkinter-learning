# Entry widget = textbox that accepts a single line of user input

from tkinter import *  # import all tkinter GUI components

def submit():
    username = entry.get()  # get the text currently inside the entry box
    print("Hello " + username)  # print in the console

def delete():
    entry.delete(0, END)  # delete characters from index 0 to the end

def backspace():
    entry.delete(len(entry.get()) - 1, END)  # delete last character using its index

window = Tk()
window.title("user input")

label = Label(window, text="username: ")  # create a label describing the entry field
label.config(font=("Consolas", 30))  # set label font
label.pack(side=LEFT)  # place the label on the left side of the window

submit_btn = Button(window, text="submit", command=submit)  # button to submit the entry text
submit_btn.pack(side=RIGHT)

delete_btn = Button(window, text="delete", command=delete)  # button to clear the entry box
delete_btn.pack(side=RIGHT)

backspace_btn = Button(window, text="backspace", command=backspace)  # button to remove last character
backspace_btn.pack(side=RIGHT)

entry = Entry()  # create the entry textbox widget
entry.config(font=('Ink Free', 50))  # change the font style and size of the text
entry.config(bg='#111111')  # set entry background color
entry.config(fg='#00FF00')  # set text color inside the entry
entry.config(width=10)  # width of the entry box measured in characters

# entry.insert(0, 'Spongebob')  # insert default text starting at index 0
# entry.config(state=DISABLED)  # disable the entry box (user cannot type)
# entry.config(show='*')  # hide typed characters (useful for passwords)

entry.pack()  # add the entry widget to the window

window.mainloop()  # start the GUI event loop (keeps the window open)
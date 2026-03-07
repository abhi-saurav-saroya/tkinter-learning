# Button example: clicking the button increases a counter and updates the label

from tkinter import *  # import all tkinter GUI components

count = 0  # variable to store how many times the button is clicked

def click():
    global count  # allows modification of the global variable 'count'
    count += 1
    label.config(text=count)  # update the label text to show the new count in the window itself

window = Tk()  # create the main application window

image = PhotoImage(file='pointer.png')  # load an image file to use on the button

button = Button(  # create the button widget and configure it at the same time
    window,  # parent window where the button will appear
    text="Click me!!!",  # text displayed on the button
    command=click,  # callback function executed when the button is clicked
    font=('Ink Free',50,'bold'),  # button font (font name, size, style)
    bg='#ff6200',  # button background color
    fg='#fffb1f',  # button text color
    activebackground='#FF0000',  # background color while the button is pressed
    activeforeground='#fffb1f',  # text color while the button is pressed
    image=image,  # image displayed on the button
    compound='bottom'  # places the text below the image
)

label = Label(window, text=count)  # label widget that displays the counter value
label.config(font=('Monospace',50))  # set the label font

label.pack()  # add the label to the window
button.pack()  # add the button to the window

window.mainloop()  # start the GUI event loop and keep the window running
# Messagebox example = popup dialog boxes used to show messages or ask the user questions

from tkinter import *
from tkinter import messagebox  # import messagebox module

def click():  # function runs when the button is clicked

    # showinfo() = basic informational popup
    messagebox.showinfo(title='Information',message='This is an informational message.')

    # showwarning() = warning popup
    messagebox.showwarning(title='Warning',message='Please check your input.')

    # showerror() = error popup
    messagebox.showerror(title='Error',message='An unexpected error occurred.')

    # askokcancel() = returns True if OK is pressed, False if Cancel is pressed
    if messagebox.askokcancel(title='Confirmation',message='Do you want to continue?'):
       print('Operation confirmed.')
    else:
       print('Operation cancelled.')

    # askretrycancel() = returns True if Retry is pressed
    if messagebox.askretrycancel(title='Retry',message='The action failed. Try again?'):
       print('Retrying the operation...')
    else:
       print('Operation cancelled.')

    # askyesno() = returns True for Yes and False for No
    if messagebox.askyesno(title='Question',message='Do you like programming?'):
       print('Nice! Programming is very useful.')
    else:
       print('That is okay. Everyone has different interests.')

    # askquestion() = returns string "yes" or "no"
    answer = messagebox.askquestion(title='Simple Question',message='Do you want to proceed?')
    if answer == 'yes':
       print('You selected yes.')
    else:
       print('You selected no.')

    # askyesnocancel() = returns True, False, or None
    answer = messagebox.askyesnocancel(title='Final Question',message='Would you like to continue?',icon='question')

    if answer == True:
        print("You chose Yes.")
    elif answer == False:
        print("You chose No.")
    else:
        print("You selected Cancel.")



window = Tk()  # create main application window
window.title("Messagebox Tutorial")

button = Button(window,text='Click Me',command=click)  # button that triggers the messageboxes
button.pack()

window.mainloop()  # start the GUI event loop
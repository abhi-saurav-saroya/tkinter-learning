# File dialog example = allows the user to choose a file and display its contents

from tkinter import *
from tkinter import filedialog  # import module for file dialogs

def openFile():  # function runs when the Open button is clicked
    # open file selection dialog
    filepath = filedialog.askopenfilename(
        title="Select File",  # title shown on the dialog window
        filetypes=(           # file type filters shown in the dialog
            ("Text File", "*.txt"),     # show .txt files
            ("Python Files", "*.py"),   # show .py files
            ("All Files", "*.*")        # show all files
        )
    )

    if filepath:  # check if the user selected a file
        file = open(filepath, 'r')  # open the file in read mode
        print(file.read())  # print file contents to the console
        file.close()  # close the file after reading

window = Tk()
window.title("File Opener")

# button that opens the file dialog
button = Button(window, text="Open", command=openFile)
button.pack()

window.mainloop()
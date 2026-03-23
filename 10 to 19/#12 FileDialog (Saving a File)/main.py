# Save file dialog example = allows the user to save text from the Text widget into a file

from tkinter import *
from tkinter import filedialog  # import module for save file dialog

def saveFile():  # function runs when the Save button is clicked
    # open the "Save As" dialog window
    file = filedialog.asksaveasfile(
        # initialdir="C:\\Users",  # starting directory shown in the dialog
        defaultextension='.txt',  # default file extension
        filetypes=[               # file format options shown to the user
            ("Text file", ".txt"),
            ("HTML file", ".html"),
            ("All files", ".*"),
            ("Python files", ".py")
        ]
    )

    if file is None:  # if the user cancels the dialog
        return

    # get all text from the Text widget (from line 1, char 0 to end)
    filetext = str(text.get(1.0, END))

    # write the text to the selected file
    file.write(filetext)

    # close the file after saving
    file.close()

window = Tk()  # create the main application window
window.title("Save File Example")

# text area where the user can type content to save
text = Text(window)
text.pack()

# button that opens the save file dialog
button = Button(window, text="Save", command=saveFile)
button.pack()

window.mainloop()
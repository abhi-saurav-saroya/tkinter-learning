# Notebook widget example = creates tabbed interface (multiple pages in one window)

from tkinter import *
from tkinter import ttk  # import themed widgets (includes Notebook)

window = Tk()  # create the main window
window.title("Notebook Example")

# create a Notebook widget (tab manager)
notebook = ttk.Notebook(window)

# create frames (each frame = one tab/page)
tab1 = Frame(notebook)  # first tab
tab2 = Frame(notebook)  # second tab

# add tabs to the notebook
notebook.add(tab1, text="Tab 1")  # label shown on tab
notebook.add(tab2, text="Tab 2")

# place the notebook in the window
notebook.pack(expand=True, fill="both")
# expand=True  # widget expands to fill extra space
# fill="both"  # fills both horizontal and vertical space

# add content inside tab 1
Label(
    tab1,
    text="Hello, this is tab #1",
    width=50,
    height=25
).pack()

# add content inside tab 2
Label(
    tab2,
    text="Goodbye, this is tab #2",
    width=50,
    height=25
).pack()

window.mainloop()
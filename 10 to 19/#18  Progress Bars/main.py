# Progressbar example = shows progress of a task (like downloading a file)

from tkinter import *  # import tkinter GUI components
from tkinter.ttk import *  # import themed widgets (includes Progressbar)
import time  # used to simulate delay

def start():  # function runs when the button is clicked
    GB = 100        # total size of the task (100 GB for simulation)
    download = 0    # amount downloaded so far
    speed = 1       # download speed per iteration

    # loop until download is complete
    while download < GB:
        time.sleep(0.05)  # pause to simulate time delay

        # update progress bar value (percentage)
        bar['value'] += (speed / GB) * 100

        download += speed  # increase downloaded amount

        # update percentage label
        percent.set(str(int((download / GB) * 100)) + "%")

        # update progress text label
        text.set(str(download) + "/" + str(GB) + " GB completed")

        window.update_idletasks()  # refresh the GUI

window = Tk()  # create the main window
window.title("Progress Bar Example")

percent = StringVar()  # stores percentage text
text = StringVar()     # stores progress text

# create progress bar widget
bar = Progressbar(
    window,
    orient=HORIZONTAL,  # horizontal bar
    length=300          # width of the bar
)
bar.pack(pady=10)

# label to show percentage completed
percentLabel = Label(window, textvariable=percent)
percentLabel.pack()

# label to show detailed progress
taskLabel = Label(window, textvariable=text)
taskLabel.pack()

# button to start the progress
button = Button(window, text="Download", command=start)
button.pack()

window.mainloop()  # start the tkinter event loop
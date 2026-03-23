import tkinter as tk

window = tk.Tk()        # instantiate the window
window.geometry("500x500")          #change window dimensions
window.title("My First GUI")        #title of window i.e., displayed on above bar

icon = tk.PhotoImage(file="logo.png")           #to change icon of window, it takes only PhotoImage format picture, so convert png into one firstlu
window.iconphoto(True, icon)           #replace icon with new one

window.config(bg="blue")        #congiguring the window's background colour

window.mainloop()
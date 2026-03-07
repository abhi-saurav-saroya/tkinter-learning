import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
window.title("My First GUI")

icon = tk.PhotoImage(file="logo.png")
window.iconphoto(True, icon)

window.configure(bg="blue")

window.mainloop()
import tkinter as tk

# Labels are area widget that hold text and/or image in a window

window = tk.Tk()
window.title("Labels")
window.geometry("700x700")

cat = tk.PhotoImage(file="cat.png")

label = tk.Label(window,            #mention the window to which this label belongs to
                 text="HELLO THERE",
                 font=("Arial", 25, 'bold', 'italic'),
                 fg="white",        #foreground
                 bg="black",         #background
                 relief="raised",     #border style
                 bd=10,                   #border width
                 padx=20,              #padding along x axis
                 pady=20,
                 image=cat,             #adding image to label using image attribute
                 compound="bottom")     #this specifies the position of image relative to the text in label
label.pack()        # .pack() packs the label in the window

label2 = tk.Label(window, text="HELLO THERE")
label2.place(x=10, y=80)        # .place() does the same but we can specify coordinates


window.mainloop()
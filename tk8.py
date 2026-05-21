from tkinter import *

root = Tk()

def greet():
    name = entry.get()
    label.config(text=f"Hello {name}")

entry = Entry(font=("Arial", 16))
entry.pack()

button = Button(text="Submit", command=greet)
button.pack()

label = Label(font=("Arial", 18))
label.pack()

root.mainloop()
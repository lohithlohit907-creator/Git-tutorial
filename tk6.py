from tkinter import *

root = Tk()

count = 0

def increase():
    global count
    count += 1
    label.config(text=f"Count: {count}")

label = Label(text="Count: 0", font=("Arial", 20))
label.pack()

button = Button(text="Increase", command=increase)
button.pack()

root.mainloop()
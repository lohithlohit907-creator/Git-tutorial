from tkinter import *

root = Tk()
root.geometry("200x300")
def show():
    name=entry.get()
    if name=="lohith":
        print("i love you")
    else:
        print(entry.get())    


entry = Entry()
entry.pack()

button = Button(text="Submit", command=show)
button.pack()

root.mainloop()
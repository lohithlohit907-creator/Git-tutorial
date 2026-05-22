from tkinter import *

root = Tk()

def show():

    data = text.get("1.0", END)

    print(data)

text = Text(height=10, width=30)

text.pack()

Button(
    text="Show Text",
    command=show
).pack()

root.mainloop()
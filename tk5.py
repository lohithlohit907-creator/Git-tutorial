from tkinter import *

root = Tk()

root.geometry("500x300")

title = Label(
    text="Kushal Sagar",
    font=("Arial", 24, "bold"),
    bg="black",
    fg="cyan",
    pady=20
)

quote = Label(
    text="I hate loosing more than i enjoy winning",
    font=("Arial", 16),
    fg="white",
    bg="black"
)
 
author=Label(
    text="--Micheal phelps",
    font="italic 10 bold",
    fg="white",
    bg="black"
) 

title.pack(fill=X)
quote.pack()
author.pack(padx=100)
root.configure(bg="black")

root.mainloop()
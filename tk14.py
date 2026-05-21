from tkinter import *

root = Tk()

root.geometry("500x400")

# ---------- HEADER FRAME ----------

header = Frame(root, bg="black")

header.pack(fill=X)

title = Label(
    header,
    text="Kushal News",
    bg="black",
    fg="white",
    font=("Arial",20,"bold"),
    pady=10
)

title.pack()

# ---------- CONTENT ----------

content = Label(
    root,
    text="Welcome to the news app",
    font=("Arial",16)
)

content.pack(pady=20)

root.mainloop()
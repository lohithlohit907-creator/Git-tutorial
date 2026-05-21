from tkinter import *

root = Tk()

root.geometry("500x400")

# TOP FRAME
top = Frame(root, bg="black")
top.pack(fill=X)

Label(top, text="TOP MENU", fg="white", bg="black").pack()

# LEFT FRAME
left = Frame(root, bg="gray", width=100)
left.pack(side=LEFT, fill=Y)

Button(left, text="Home").pack(pady=10)

Button(left, text="Profile").pack(pady=10)

# MAIN CONTENT
main = Frame(root, bg="white")
main.pack()

Label(main, text="Main Content Area").pack()

root.mainloop()
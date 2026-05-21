from tkinter import *

root = Tk()

root.geometry("400x300")

frame = Frame(root, bg="lightblue", padx=20, pady=20)

frame.pack(pady=50)

Label(frame, text="Username").grid(row=0,column=0)

Entry(frame).grid(row=0,column=1)

Label(frame, text="Password").grid(row=1,column=0)

Entry(frame, show="*").grid(row=1,column=1)

Button(frame, text="Login").grid(row=2,column=1,pady=10)

root.mainloop()
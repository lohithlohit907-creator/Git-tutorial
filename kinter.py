from tkinter import *
from PIL import Image,ImageTk

lohith_root= Tk()
# widthxheight
lohith_root.geometry("500x400")
# width,heigh
lohith_root.minsize(900,600)

lohith_root.maxsize(1000,800)
lohith=Label(text="welcome to lohit's GUI")
lohith.pack()
# photo=PhotoImage(file=r"C:\Users\kushal sagar\OneDrive\Documents\lohith .jpeg")
# for jpg images
image=Image.open(r"C:\Users\kushal sagar\OneDrive\Documents\lohith .jpeg")
photo=ImageTk.PhotoImage(image)
jeevan=Label(image=photo)
jeevan.pack()   

lohith_root.mainloop()


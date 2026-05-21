from tkinter import *
from PIL import Image, ImageTk

lohith_root = Tk()

# Window size
lohith_root.geometry("500x400")

# Minimum and maximum size
lohith_root.minsize(900, 600)
lohith_root.maxsize(1000, 800)

# ---------------- NEWS ----------------

file = open("lohit.txt", "r")
data = file.read()
file.close()

news = Label(
    text=data,
    font=("Times New Roman", 14, "bold"),
    bg="white",
    fg="black",
    wraplength=800,
    justify=LEFT,
    padx=20,
    pady=20
)

news.pack(side=TOP, fill=X)
# frame = Frame(lohith_root)
# frame.pack()

# news.pack(in_=frame, side=LEFT)
# jeevan.pack(in_=frame, side=RIGHT)

# ---------------- IMAGE ----------------

image = Image.open(r"C:\Users\kushal sagar\OneDrive\Documents\lohith .jpeg")

# Resize image (optional)
image = image.resize((500, 500))

photo = ImageTk.PhotoImage(image)

jeevan = Label(image=photo)
jeevan.image=photo
jeevan.pack()

lohith_root.mainloop()
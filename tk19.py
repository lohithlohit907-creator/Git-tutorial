from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("500x500")

root.configure(bg="black")

# ---------- TOP FRAME ----------

top = Frame(root, bg="black")

top.pack(fill=X)

Label(
    top,
    text="LOHITH NEWS",
    font=("Arial",20,"bold"),
    bg="black",
    fg="cyan"
).pack(pady=10)

# ---------- LEFT FRAME ----------

left = Frame(root, bg="black")

left.pack(fill=BOTH, expand=True)

# ---------- IMAGE ----------

image = Image.open(
    r"C:\Users\kushal sagar\OneDrive\Documents\lohith .jpeg"
)

image = image.resize((250,250))

photo = ImageTk.PhotoImage(image)

img_label = Label(left, image=photo, bg="black")

img_label.image = photo

img_label.pack(pady=10)

# ---------- NEWS ----------

file = open("lohit.txt", "r")

data = file.read()

file.close()

news = Label(
    left,
    text=data,
    bg="white",
    fg="black",
    wraplength=400,
    justify=LEFT,
    padx=10,
    pady=10,
    font=("Arial",12)
)

news.pack(pady=10)

root.mainloop()
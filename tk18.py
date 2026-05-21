from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.geometry("500x500")
root.configure(bg="black")
    # top frame
top=Frame(root, bg="black")
top.pack(fill=X)

Label(top,text="LOHITH NEWS",font="Airal 20 bold" ,bg="black",fg="cyan").pack(pady=10)

        # image
image = Image.open(r"C:\Users\kushal sagar\OneDrive\Documents\lohith .jpeg")
image = image.resize((250,250))

photo = ImageTk.PhotoImage(image)
        # news
file = open("lohit.txt", "r")
data = file.read()
file.close()




        # left frame
left=Frame(root,bg="lightblue")
left.pack(side=LEFT,fill=Y)

Label(left,image=photo,bg="black",fg="white").pack()
    # bottom frame
# bottom=Frame(root,bg="darkgray")
# bottom.pack(side=BOTTOM,fill=X)

Label(left,text=data,bg="white",fg="black").pack()






root.mainloop()
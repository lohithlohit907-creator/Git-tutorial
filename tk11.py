# # from tkinter import *

# # root = Tk()

# # Label(text="First").pack()
# # Label(text="Second").pack()
# # Button(text="Button").pack()

# # root.mainloop()

# # from tkinter import *

# # root = Tk()

# # Label(text="LEFT", bg="red").pack(side=LEFT)
# # # Label(text="RIGHT", bg="blue").pack(side=RIGHT)
# # Label(text="News", bg="yellow").pack(fill=X)

# # root.mainloop()

# from tkinter import *

# root = Tk()

# root.geometry("500x300")

# Button(text="Home").pack(side=LEFT)
# Button(text="About").pack(side=LEFT)
# Button(text="Contact").pack(side=LEFT)

# root.mainloop()

from tkinter import *

root = Tk()

root.geometry("600x600")

Label(text="Name").grid(row=0, column=0)
Entry().grid(row=0, column=1)

Label(text="Age").grid(row=1, column=0)
Entry().grid(row=1, column=1)

Label(text="status").grid(row=2, column=0)
Entry().grid(row=2,column=1)


root.mainloop()
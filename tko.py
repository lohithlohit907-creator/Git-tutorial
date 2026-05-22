from tkinter import *

root=Tk()
root.geometry("500x500")
root.configure(bg="black")
        # function
def love():
    he=entry.get()
    she=entry2.get()
    label.config(text=f"{he} loves {she}")

    # name label
name=Label(
    text="enter your name",
    font="Arial 16 bold",
    bg="black",
    fg="white"
)

name.pack(pady=5)

    # name entry

entry=Entry(
    font="Airal 16 bold",
    bg="black",
    fg="white"
)

entry.pack(pady=5)

        # name2 label

name2=Label(
    text="enter her name",
    font="Airal 16 bold",
    bg="black",
    fg="white"
)

name2.pack(pady=5)

        # name2 entry
entry2=Entry(
    font="Arial 16 bold",
    bg="black",
    fg="white"
)

entry2.pack(pady=5)
    # button
button=Button(
    text="submit",
    command=love,
    font="Airal 16 bold"
)

button.pack(pady=5)

        # result label
label=Label(
    font="Airal 16 bold",
    bg="black",
    fg="red"
)

label.pack(pady=10)    




root.mainloop()

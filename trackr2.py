from tkinter import *

root=Tk()
root.geometry("400x400")
# root.configure(bg="black")
root.title("Lohith's tracker")
        # title
title=Label(
    root,
    text="DAILY TRACKER",
    font="Airal 20 bold"

)

title.pack(pady=20)
        # variables
wake=IntVar()
work=IntVar()
workout=IntVar()
read=IntVar()
nofap=IntVar()

        # checkbuttons
Checkbutton(
    root,
    text="Wake up before 6",
    variable=wake,
    font="Airal 16 bold"
).pack(anchor="w")

Checkbutton(
    root,
    text="work",
    variable=work,
    font="Airal 16 bold"
).pack(anchor="w")

Checkbutton(
    root,
    text="workout",
    variable=workout,
    font="Airal 16 bold"
).pack(anchor="w")

Checkbutton(
    root,
    text="read 10 pages",
    variable=read,
    font="Airal 16 bold"
).pack(anchor="w")

Checkbutton(
    root,
    text="no fap",
    variable=nofap,
    font="Airal 16 bold"
).pack(anchor="w")

    # save function
def save():
    file=open("tracker.txt","w")

    file.write(f"wake up before 6:{wake.get()}\n")

    file.write(f"work :{work.get()}\n")

    file.write(f"workout:{workout.get()}\n")

    file.write(f"read 10 pages:{read.get()}\n")

    file.write(f"no fap:{nofap.get()}\n")

    file.close()

    status.config(
        text="progress saved",
        font="Arial 16 bold"
    )
    
    # save Button
Button(
    text="save progress",
    command=save,
    font="Airal 10 bold"

).pack(pady=20)

    # status
status=Label(
    font="Airal 16 bold",
    fg="green"

)

status.pack()

root.mainloop()


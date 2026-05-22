from tkinter import *

root = Tk()

root.geometry("400x400")

root.title("Daily Tracker")

# ---------- TITLE ----------

title = Label(
    root,
    text="DAILY TRACKER",
    font=("Arial",20,"bold")
)

title.pack(pady=20)

# ---------- VARIABLES ----------

wake_var = IntVar()

work_var = IntVar()

workout_var = IntVar()

read_var = IntVar()

nofap_var = IntVar()

# ---------- CHECKBUTTONS ----------

Checkbutton(
    root,
    text="Wake up before 6",
    variable=wake_var,
    font=("Arial",14)
).pack(anchor="w")

Checkbutton(
    root,
    text="Work 6 hrs",
    variable=work_var,
    font=("Arial",14)
).pack(anchor="w")

Checkbutton(
    root,
    text="Workout",
    variable=workout_var,
    font=("Arial",14)
).pack(anchor="w")

Checkbutton(
    root,
    text="Read 10 pages",
    variable=read_var,
    font=("Arial",14)
).pack(anchor="w")

Checkbutton(
    root,
    text="No Fap",
    variable=nofap_var,
    font=("Arial",14)
).pack(anchor="w")

# ---------- SAVE FUNCTION ----------

def save_data():

    file = open("tracker.txt","w")

    file.write(
        f"Wake Up Before 6: {wake_var.get()}\n"
    )

    file.write(
        f"Work 6 Hours: {work_var.get()}\n"
    )

    file.write(
        f"Workout: {workout_var.get()}\n"
    )

    file.write(
        f"Read 10 Pages: {read_var.get()}\n"
    )

    file.write(
        f"No Fap: {nofap_var.get()}\n"
    )

    file.close()

    status.config(text="Progress Saved!")

# ---------- SAVE BUTTON ----------

Button(
    root,
    text="Save Progress",
    command=save_data,
    font=("Arial",14)
).pack(pady=20)

# ---------- STATUS ----------

status = Label(font=("Arial",12))

status.pack()

root.mainloop()
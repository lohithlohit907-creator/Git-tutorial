from tkinter import *

root = Tk()

root.geometry("500x500")

root.title("Productivity Tracker")

root.configure(bg="#121212")

# ---------- TITLE ----------

title = Label(
    root,
    text="DAILY PRODUCTIVITY TRACKER",
    font=("Arial",20,"bold"),
    bg="#121212",
    fg="cyan"
)

title.pack(pady=20)

# ---------- VARIABLES ----------

wake_var = BooleanVar()

work_var = BooleanVar()

workout_var = BooleanVar()

read_var = BooleanVar()

nofap_var = BooleanVar()

# ---------- PROGRESS LABEL ----------

progress_label = Label(
    root,
    text="Completed: 0/5",
    font=("Arial",14,"bold"),
    bg="#121212",
    fg="white"
)

progress_label.pack(pady=10)

# ---------- STATUS LABEL ----------

status = Label(
    root,
    font=("Arial",16,"bold"),
    bg="#121212",
    fg="cyan"
)

status.pack(pady=10)

# ---------- UPDATE FUNCTION ----------

def update_progress():

    completed = 0

    if wake_var.get():
        completed += 1

    if work_var.get():
        completed += 1

    if workout_var.get():
        completed += 1

    if read_var.get():
        completed += 1

    if nofap_var.get():
        completed += 1

    progress_label.config(
        text=f"Completed: {completed}/5"
    )

    if completed == 5:

        status.config(
            text="Perfect Day 🔥"
        )

    elif completed >= 3:

        status.config(
            text="Good Progress 💪"
        )

    else:

        status.config(
            text="Keep Going 🚀"
        )

# ---------- CHECKBOXES ----------

Checkbutton(
    root,
    text="Wake up before 6",
    variable=wake_var,
    command=update_progress,
    font=("Arial",14),
    bg="#121212",
    fg="white",
    selectcolor="#121212"
).pack(anchor="w", padx=40, pady=5)

Checkbutton(
    root,
    text="Work 6 hrs",
    variable=work_var,
    command=update_progress,
    font=("Arial",14),
    bg="#121212",
    fg="white",
    selectcolor="#121212"
).pack(anchor="w", padx=40, pady=5)

Checkbutton(
    root,
    text="Workout",
    variable=workout_var,
    command=update_progress,
    font=("Arial",14),
    bg="#121212",
    fg="white",
    selectcolor="#121212"
).pack(anchor="w", padx=40, pady=5)

Checkbutton(
    root,
    text="Read 10 pages",
    variable=read_var,
    command=update_progress,
    font=("Arial",14),
    bg="#121212",
    fg="white",
    selectcolor="#121212"
).pack(anchor="w", padx=40, pady=5)

Checkbutton(
    root,
    text="No Fap",
    variable=nofap_var,
    command=update_progress,
    font=("Arial",14),
    bg="#121212",
    fg="white",
    selectcolor="#121212"
).pack(anchor="w", padx=40, pady=5)

root.mainloop()
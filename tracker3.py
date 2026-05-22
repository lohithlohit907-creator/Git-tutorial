from tkinter import *
from datetime import date

root = Tk()

root.geometry("500x600")

root.title("Lohith's Productivity Tracker")

root.configure(bg="#121212")
today = str(date.today())

   # variables
wake=BooleanVar()
work=BooleanVar()
workout=BooleanVar()
read=BooleanVar()
nofap=BooleanVar()
water=BooleanVar()

# ----------- title label----------------
title=Label(
    root,
    text=" DAILY PRODUCTIVITY TRACKER",
    font="Airal 20 bold",
    bg="#121212",
    fg="cyan"
)
title.pack(pady=20)

    
#-------------process label-------------
progress=Label(
    root,
    text="completed 0/6",
    font="Airal 16 bold",
    bg="#121212",
    fg="white"
)
progress.pack(pady=10)

# -----------STATUS LABEL--------------
status=Label(
    root,
    font="Airal 18 bold",
    bg="#121212",
    fg="cyan"
)
status.pack(pady=10)

#-----------streak label---------------
streak_label = Label(
    root,
    text="Streak: 0 🔥",
    font=("Arial",16,"bold"),
    bg="#121212",
    fg="orange"
)

streak_label.pack(pady=10)

# -----------FUNCTIONS-------------------

# -----------UPDATE FUNCTIOM-------------
def update():

    completed=0

    if wake.get():
        completed+=1
    
    if work.get():
        completed+=1

    if workout.get():
        completed+=1
    
    if read.get():
        completed+=1

    if nofap.get():
        completed+=1

    if water.get():
        completed+=1

    progress.config(
        text=f"COMPLETED:{completed}/6"
    )
    # MOTIVATION

    if completed==6:

        status.config(
            text="thats sharky 🦈"
        )

    elif completed==5:
        status.config(
            text="CONSISTENCY beats talent 💪"
        )
    elif completed==4:
        status.config(
            text="DISCIPLINE😈"
        )

    elif completed==3:
        status.config(
            text="not enough bro👊"
        )       
    elif completed==2:
        status.config(
            text="no EXCUESS😤⚠️"
        )
    elif completed==1:
        status.config(
            text="there is no tommorow"
        )
    else:
        status.config(
            text="LOOSER👊"
        )

# ----------SAVE DATE FUNCTION------------
def save_data():

    file = open("tracker_history.txt","a")

    file.write(
        f"{today}|"
        f"{wake.get()}|"
        f"{work.get()}|"
        f"{workout.get()}|"
        f"{read.get()}|"
        f"{nofap.get()}|"
        f"{water.get()}\n"
    )

    file.close()

    status.config(
        text="Progress Saved ✅"
    )

# ---------CHECKBOXES----------------
Checkbutton(
    root,
    text="wake up before 6",
    variable=wake,
    command=update,
    font="Airal 16",
    bg="#121212",
    fg="white",
    selectcolor="#121212"
).pack(anchor="w",padx=40,pady=5)

Checkbutton(
    root,
    text="work min 6 hrs",
    variable=work,
    command=update,
    font="Airal 16",
    bg="#121212",
    fg="white",
    selectcolor="#121212"
).pack(anchor="w",padx=40,pady=5)

Checkbutton(
    root,
    text="workout",
    variable=workout,
    command=update,
    font="Airal 16",
    bg="#121212",
    fg="white",
    selectcolor="#121212"
).pack(anchor="w",padx=40,pady=5)

Checkbutton(
    root,
    text="read 10 pages",
    variable=read,
    command=update,
    font="Airal 16",
    bg="#121212",
    fg="white",
    selectcolor="#121212"
).pack(anchor="w",padx=40,pady=5)

Checkbutton(
    root,
    text="no FAP",
    variable=nofap,
    command=update,
    font="Airal 16",
    bg="#121212",
    fg="white",
    selectcolor="#121212"
).pack(anchor="w",padx=40,pady=5)

Checkbutton(
    root,
    text="drink 4ltr of water",
    variable=water,
    command=update,
    font="Airal 16",
    bg="#121212",
    fg="white",
    selectcolor="#121212"
).pack(anchor="w",padx=40,pady=5)
   
# -------------LOAD FUNCTION------------
def load_data():

    try:

        file = open("tracker_history.txt","r")

        data = file.readlines()

        file.close()

        saved_date = data[0].strip()

        # CHECK DATE

        if saved_date == today:

            wake.set(data[1].strip() == "True")

            work.set(data[2].strip() == "True")

            workout.set(data[3].strip() == "True")

            read.set(data[4].strip() == "True")

            nofap.set(data[5].strip() == "True")

            water.set(data[6].strip() == "True")

            update()

        else:

            print("New Day Started")

    except FileNotFoundError:

        print("No previous data found")

    try:

        file = open("tracker_history.txt","r")

        data = file.readlines()

        file.close()

        wake.set(data[1].strip() == "True")

        work.set(data[2].strip() == "True")

        workout.set(data[3].strip() == "True")

        read.set(data[4].strip() == "True")

        nofap.set(data[5].strip() == "True")

        water.set(data[6].strip() == "True")

        update()

    except:

        print("No previous data found")

# -----------STREAK FUNCTION-------------
def calculate_streak():

    try:

        file = open("tracker_history.txt","r")

        lines = file.readlines()

        file.close()

        streak = 0

        for line in reversed(lines):

            data = line.strip().split("|")

            completed = data.count("True")

            if completed >= 5:

                streak += 1

            else:

                break

        streak_label.config(
            text=f"Streak: {streak} 🔥"
        )

    except FileNotFoundError:

        streak_label.config(
            text="Streak: 0 🔥"
        )

# -----------------BUTTON-----------------
Button(
    root,
    text="Save Progress",
    command=lambda:[save_data(),calculate_streak()],
    font=("Arial",14,"bold"),
    bg="cyan"
).pack(pady=20)

# -------------CALLING FUNCTION------------
load_data()
calculate_streak()


root.mainloop()
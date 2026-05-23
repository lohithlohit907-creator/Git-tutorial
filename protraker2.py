from tkinter import *
from datetime import date
import matplotlib.pyplot as plt

root = Tk()

root.geometry("550x650")

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
status_label=Label(
    root,
    font="Airal 18 bold",
    bg="#121212",
    fg="cyan"
)
status_label.pack(pady=10)

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

        status_label.config(
            text="thats sharky 🦈"
        )

    elif completed==5:
        status_label.config(
            text="CONSISTENCY beats talent 💪"
        )
    elif completed==4:
        status_label.config(
            text="DISCIPLINE😈"
        )

    elif completed==3:
        status_label.config(
            text="not enough bro👊"
        )       
    elif completed==2:
        status_label.config(
            text="no EXCUESS😤⚠️"
        )
    elif completed==1:
        status_label.config(
            text="there is no tommorow"
        )
    else:
        status_label.config(
            text="LOOSER👊"
        )

# ----------SAVE DATE FUNCTION------------
def save_data():

    file = open("trackme.txt","a")

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

    status_label.config(
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

        file = open("trackme.txt","r")

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

        file = open("trackme.txt","r")

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

        file = open("trackme.txt","r")

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

# -----------STATISTICS FUNCTION------
def stats():

    try:

        file=open("trackme.txt","r")
        lines=file.readlines()
        file.close()

        totaldays=len(lines)
        sharkysday=0
        best_streak=0
        current_streak=0

        for line in lines:
            data=line.strip().split("|")

            completed=data.count("True")

            # sharky's day

        if completed==6:    
            sharkysday+=1

        # streak system

        if completed>=5:
            current_streak+=1   

        else:
            current_streak=0

        # best streak
        if current_streak>best_streak:
            best_streak=current_streak
        completion_rate=(
        sharkysday/totaldays
    )*100

        status_label.config(
        text=
        f"Total days:{totaldays}\n"
        f"sharky's days:{sharkysday}\n"
        f"completion rate:{completion_rate}\n"
        f"best streaks:{best_streak}\n"
    )
    except FileNotFoundError:
        status_label.config(
            text="no statistics yet"
    )
        
# ---------------GRAPH FUNCTION-------------------
def show_graph():

    try:

        file = open("trackme.txt","r")

        lines = file.readlines()

        file.close()

        days = []
        scores = []

        for line in lines:

            data = line.strip().split("|")

            completed = data.count("True")

            days.append(data[0])

            scores.append(completed)

        print(days)
        print(scores)

        plt.plot(days,scores)

        plt.title("Consistency Graph")

        plt.xlabel("Days")

        plt.ylabel("Completed Goals")

        plt.show()

    except FileNotFoundError:

        print("No history file found")
# -----------------BUTTON-----------------
Button(
    root,
    text="Save Progress",
    command=lambda:[save_data(),calculate_streak(),stats()],
    font=("Arial",14,"bold"),
    bg="cyan"
).pack(pady=20)

# ----------------Graph button----------------
Button(
    root,
    text="Show Graph 📈",
    command=show_graph,
    font=("Arial",14,"bold"),
    bg="orange"
).pack(pady=10)
# -------------CALLING FUNCTION------------
load_data()
calculate_streak()

root.mainloop()
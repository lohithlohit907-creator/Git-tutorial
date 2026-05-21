from tkinter import *

root = Tk()

root.geometry("400x500")

root.configure(bg="black")

# ---------------- FUNCTION ----------------

def greet():
    name = entry.get()
    age = entry2.get()

    label.config(
        text=f"Hello {name}, your age is {age}"
    )

# ---------------- NAME LABEL ----------------

name_label = Label(
    text="Enter Your Name",
    font=("Arial", 14, "bold"),
    bg="black",
    fg="white"
)

name_label.pack(pady=5)

# ---------------- NAME ENTRY ----------------

entry = Entry(
    font=("Arial", 16),
    bg="black",
    fg="white"
)

entry.pack(pady=5)

# ---------------- AGE LABEL ----------------

age_label = Label(
    text="Enter Your Age",
    font=("Arial", 14, "bold"),
    bg="black",
    fg="white"
)

age_label.pack(pady=5)

# ---------------- AGE ENTRY ----------------

entry2 = Entry(
    font=("Arial", 16),
    bg="black",
    fg="white"
)

entry2.pack(pady=5)

# ---------------- BUTTON ----------------

button = Button(
    text="Submit",
    command=greet,
    font=("Arial", 14, "bold")
)

button.pack(pady=10)

# ---------------- RESULT LABEL ----------------

label = Label(
    font=("Arial", 18),
    bg="black",
    fg="cyan"
)

label.pack(pady=20)

root.mainloop()
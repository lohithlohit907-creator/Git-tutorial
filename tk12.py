from tkinter import *

root = Tk()

root.geometry("350x250")
root.configure(bg="black")

# ---------- FUNCTION ----------

def login():

    username = user_entry.get()
    password = pass_entry.get()

    if username=="lohith" and password=="1072008":

        result.config(
            text=(f"welcome {username}"),
            fg="green"
        )

    else:

        result.config(
            text="Access Denied",
            fg="red"
        )

# ---------- LABELS ----------

Label(text="Username").grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

Label(text="Password").grid(
    row=1,
    column=0
)

# ---------- ENTRIES ----------

user_entry = Entry()
user_entry.grid(row=0,column=1)

pass_entry = Entry(show="*")
pass_entry.grid(row=1,column=1)

# ---------- BUTTON ----------

Button(
    text="Login",
    command=login
).grid(
    row=2,
    column=1,
    pady=10
)

# ---------- RESULT LABEL ----------

result = Label(font=("Arial",14,"bold"))

result.grid(
    row=3,
    column=1
)

root.mainloop()
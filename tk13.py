from tkinter import *

root=Tk()

root.geometry("350x250")
root.configure(bg="black")
     
    # function
def login():
    username=user_entry.get()
    password=pass_entry.get()

    if username=="lohith" and password=="1072008":
        result.config(
            text="ACCESS GRANTED",
            fg="green",
            font="Airal 16 bold"
        )
    else:
        result.config(
            text="ACCESS DENAID",
            fg="red",
            font="Airal 16 bold"
        )

        # Labels

Label(text="username").grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

Label(text="password").grid(
    row=1,
    column=0
)

    #  Entries
user_entry=Entry()
user_entry.grid(
    row=0,
    column=1
)

pass_entry=Entry(show="*")
pass_entry.grid(
    row=1,
    column=1
)

        # buttons
button=Button(
    text="login",
    # fg="white",
    command=login
).grid(
    row=2,
    column=1
)


        #result
result=Label(font="Airal 14 bold")

result.grid(
    row=3,
    column=1
)


root.mainloop()
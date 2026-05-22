from tkinter import *

root = Tk()

root.geometry("500x400")

# ---------- SAVE FUNCTION ----------

def save_note():

    data = text.get("1.0", END)

    file = open("notes.txt","w")

    file.write(data)

    file.close()

    status.config(text="Note Saved!")

# ---------- TEXT AREA ----------

text = Text(
    font=("Arial",14),
    height=15,
    width=40
)

text.pack(pady=20)

# ---------- BUTTON ----------

Button(
    text="Save",
    command=save_note
).pack()

# ---------- STATUS ----------

status = Label(font=("Arial",12))

status.pack()

root.mainloop()
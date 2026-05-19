import tkinter as tk
# import time
# from plyer import notification

# # Create window 😎🔥
# window = tk.Tk()

# window.title("Drink Water Reminder")
# window.geometry("400x200")


# # Label 😳🔥
# label = tk.Label(
#     window,
#     text="💧 Drink Water Reminder 😎🔥",
#     font=("Arial", 16)
# )

# label.pack(pady=20)


# # Reminder function 😈🔥
# def remind():

#     current_time = time.strftime("%I:%M %p")

#     notification.notify(
#         title="💧 Drink Water Reminder",
#         message="Time to drink water bro 😎🔥",
#         timeout=5
#     )

#     print(f"[{current_time}] 💧 Time to drink water")

#     # Run again after 5 seconds 😳🔥
#     window.after(5000, remind)


# # Start button 😎🔥
# button = tk.Button(
#     window,
#     text="Start Reminder",
#     font=("Arial", 14),
#     command=remind
# )

# button.pack(pady=20)


# # Keep GUI alive 😎🔥
# window.mainloop()
# import tkinter as tk
# import time
# from plyer import notification

# window=tk.Tk()
# window.title("drink water remainder")
# window.geometry("400x200")
# label = tk.Label(
#     window,
#     text="💧 Drink Water Reminder 😎🔥",
#     font=("Arial", 16)
# )
# label.pack(pady=20)
# def remind():

#     current_time = time.strftime("%I:%M %p")

#     notification.notify(
#         title="💧 Drink Water Reminder",
#         message="Time to drink water bro 😎🔥",
#         timeout=5
#     )

#     print(f"[{current_time}] 💧 Time to drink water")

#     # Run again after 5 seconds 😳🔥
#     window.after(5000, remind)

# button=tk.Button(
#     window,
#     text="start remainder",
#     font=("Bold",15),
#     command=remind


# )

# button.pack(pady=20)  
# def input():
#     time=(inputbox*60)
# inputbox=tk.Entry(
#     window,
#     text="enter time in minutes",
#     font=("Areal",20),
#     command=input

# )
# inputbox.pack(pady=30)
# window.mainloop()
import tkinter as tk
import time
from plyer import notification

# Create main window 😎🔥
window = tk.Tk()

window.title("Drink Water Reminder")
window.geometry("400x250")


# Heading label 😳🔥
label = tk.Label(
    window,
    text="💧 Drink Water Reminder",
    font=("Arial", 18)
)

label.pack(pady=10)


# Instruction label 😎🔥
label2 = tk.Label(
    window,
    text="Enter time in minutes:",
    font=("Arial", 12)
)

label2.pack()


# Input box 😈🔥
inputbox = tk.Entry(
    window,
    font=("Arial", 14)
)

inputbox.pack(pady=10)


# Reminder function 😳🔥
def remind():

    current_time = time.strftime("%I:%M %p")

    notification.notify(
        title="💧 Drink Water Reminder",
        message="Time to drink water bro 😎🔥",
        timeout=5
    )

    print(f"[{current_time}] 💧 Time to drink water")

    # Repeat again after selected time 😈🔥
    window.after(delay_time, remind)


# Start button function 😎🔥
def start_reminder():

    global delay_time

    # Get user input 😳🔥
    minutes = int(inputbox.get())

    # Convert minutes → milliseconds 😈🔥
    delay_time = minutes * 60 * 1000

    print(f"Reminder started for every {minutes} minutes 😎🔥")

    # Start reminder 😳🔥
    remind()


# Button 😈🔥
button = tk.Button(
    window,
    text="Start Reminder",
    font=("Arial", 14),
    command=start_reminder
)

button.pack(pady=20)


# Keep GUI running 😎🔥
window.mainloop()





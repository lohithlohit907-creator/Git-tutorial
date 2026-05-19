
# create folders


# os.makedirs("pdfs", exist_ok=True)
# os.makedirs("songs", exist_ok=True)
# os.makedirs("textfiles", exist_ok=True)

# get all files
# import shutil
# import os
# os.makedirs("backup", exist_ok=True)

# files = os.listdir()

# print(files)
# for file in files:
#     if os.path.isfile(file):
#      shutil.copy(file,"backup")
# print("file copied sucessfully")
# create backup folder

# # 
# import shutil
# import os
# files=os.listdir()
# print(files)
# for file in files:
#     if os.path.isfile(file):
#       os.remove(file)
      
# print("files removed sucessfully")

# import time
# from plyer import notification

# while True:

#     )
    
# import tkinter as tk
# import time
# from plyer import notification
# # Create main window 😎🔥
# window = tk.Tk()

# # Window title 😈🔥
# window.title("Drink Water Reminder")

# # Window size 😎🔥
# window.geometry("400x200")

# # Label 😳🔥
# label = tk.Label(
#     window,
#     text="💧 Drink Water Reminder 😎🔥",
#     font=("Arial", 16)
# )

# label.pack(pady=20)


# # Function for button 😈🔥
# def remind():
#     while True:
#       time.sleep(5)

#       current_time = time.strftime("%I:%M %p")

#       notification.notify(
#           title="💧 Drink Water Reminder",
#           message="Time to drink water bro 😎🔥",
#           timeout=5
#       )

#       print(f"[{current_time}] 💧 Time to drink water")

#       print("💧 Time to drink water bro 😎🔥")


# # Button 😳🔥
# button = tk.Button(
#     window,
#     text="Start Reminder",
#     font=("Arial", 14),
#     command=remind
# )

# button.pack(pady=20)

# # Keep window running 😎🔥
# window.mainloop()

# import tkinter as tk
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
# import re

# text = "My marks are 95, 88 and 76 mt age is 18"

# numbers = re.findall(r"\d+", text)
# for number in numbers:
#     print(number)

# import re

# text ="lohith phone number is 7022370292\n kushal phone number is 9141200277\n hinatas phone number is +918861212631"


# numbers= re.findall(r"\d+", text)
# for number in numbers:
#     if len(number)==10:
#      print(number)

# print(match.group())
# import re

# text = "I love you hemila"

# new_text = re.sub("hemila", "bagyashree", text)

# print(new_text)
# import re

# text = "apple,banana,mango"

# items = re.split(",", text)

# print(type(items))
# for item in items:
#     print(item)
# import re

# text = """
# lohith phone number is 7022370292
# kushal phone number is 9141200277
# hinata phone number is +918861212631
# """

# # Find exactly 10 digits 😈🔥
# numbers = re.findall(r"\d{10}", text)

# for number in numbers:
#     print(number)
# import re

# text = """
# lohith phone number is 7022370291
# kushal phone number is 9141200277
# hinata phone number is +918861212631
# """

# numbers = re.findall(r"\b\d{10}\b", text)

# for number in numbers:
#     print(number)

# import re

# text = """
# lohith's email id is lohithlohit907@gmail.com
# kushal's email id is kushalsagar@gmail.com
# hinata's email id is hinatanaruto@gmail.com
# """

# emails = re.findall(r"\w+@\w+\.com", text)

# for email in emails:
#     print(email)

# import re
# text="you are stupid"
# new_text=re.sub("stupid","*****",text)
# print(new_text)
# import re

# password = input("Enter password: ")

# # Search for number 😎🔥
# number = re.search(r"\d", password)

# # Search for uppercase letter 😈🔥
# uppercase = re.search(r"[A-Z]", password)

# if number and uppercase:
#     print("✅ Strong Password 😎🔥")

# else:
#     print("❌ Weak Password 😭🔥")
# import time
# import asyncio

# async def task1():
#     print("Task 1 started 😎🔥")
#     await asyncio.sleep(3)
#     print("Task 1 finished 😳🔥")


# async def task2():
#     print("Task 2 started 😎🔥")
#     await asyncio.sleep(3)
#     print("Task 2 finished 😳🔥")

# async def main():
#     await asyncio.gather(task1(),task2())

# asyncio.run(main())

# import time

# def task1():
#     print("Task 1 started 😎🔥")
#     time.sleep(3)
#     print("Task 1 finished 😳🔥")


# def task2():
#     print("Task 2 started 😎🔥")
#     time.sleep(3)
#     print("Task 2 finished 😳🔥")


# task1()
# task2()
# import asyncio

# async def hello():
#     print("Hello 😎🔥")

#     await asyncio.sleep(2)

#     print("Bye 😳🔥")


# asyncio.run(hello())

# import asyncio

# async def movie():
#     print("downloading movie")

#     await asyncio.sleep(5)

#     print("movie downloaded")

# async def music():
#     print("downloading music")

#     await asyncio.sleep(2)

#     print("music downloaded")

# async def game():
#     print("downloading game")

#     await asyncio.sleep(7)

#     print("game downloaded")

# async def main():
#     print("starting all downloads 😎🔥")
#     await asyncio.gather(movie(),music(),game())
#     print("all downloads complete")

# asyncio.run(main())

import asyncio
import time

async def pizza():
    print("ordered pizza ")

    await asyncio.sleep(5)

    print("pizza delivered 2nd because it takes 5 sec to make it ")


async def burger():
    print("ordered burger")

    await asyncio.sleep(10)

    print("burger delivered last because it takes more time to make it")


async def juice():
    print("ordered juice ")

    await asyncio.sleep(1)

    print("juice delivered istantly becuse it is already there in the fridge ")


async def main():
    print("order placed ")

    await asyncio.gather(pizza(),burger(),juice())
    

start = time.time()
asyncio.run(main())
end = time.time()
print(end-start)


    











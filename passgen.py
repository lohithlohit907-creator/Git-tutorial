import random

password=""
length=int(input("enter the length of password:"))

chars="123456789abcdefghijklmnopqrstuvwxyz@#$%^&*()_+"

for i in range(length):
    letters=random.choice(chars)

    password+=letters

print("PASSWORD GENERATED")
print(password)


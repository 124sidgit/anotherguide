#import these two modules random and time
import random
import time

print("//WELCOME TO PASSWORD GERERATOR PROGRAM\\\\")
char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

number=int(input("How many Password you want to generate:"))
time.sleep(1)
length=int(input("And what is the length of each password:"))
time.sleep(1)
print("\nSo here are your Passwords!")

for num in range(number):
    password=""
    for len in range(length):
        password += random.choice(char)
    print(password) 
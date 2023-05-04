#!/usr/bin/python3

# Write a Python program that asks the user to enter their name and age, and then prints a message
# saying "Hello, [name]! You are [age] years old."
# Write your program below

name, age = input("Enter name and age: ").split()
age = int(age)

print(f"Hello {name}! You are {age:d} years old.")

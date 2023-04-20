#!/usr/bin/python3

# Write a Python program that asks the user to enter their name and age, and then prints a message
# saying "Hello, [name]! You are [age] years old."
# Write your program below

# SOLUTION


name = input("Enter your name: ").capitalize()
age = int(input("How old are you? "))

print(f"Hello {name}! You are {age} years old.")

#!/usr/bin/python3

# Write a program that asks the user to input a string and then prints out each character in the string on a new line.
# Write your program below

name = input("Enter your first name: ").capitalize()
print(f"The characters in your name are: ")
for char in name:
    print(char)
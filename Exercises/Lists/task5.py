#!/usr/bin/python3

# Write a Python program to check if a given element exists in a list.
# Write your program below

my_list = [100, 50, 76, 38.2, "orange", "mango"]

check = input("Enter an element to check: ").lower()
if check in my_list:
    print(f"{check} is present in the list")
else:
    print(f"{check} does not exist in the list.")
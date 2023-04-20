#!/usr/bin/python3


# Write a Python program to check whether a given key already exists in a dictionary.

# Write your program below
user = {
    "name" : "John Smith",
    "gender" : "Male",
    "age" : 25,
    "job" : "Engineer",
    "country" : "Nigeria"
    }
check = input("Enter key to check: ").lower()
if check in user:
    print(f"The key \"{check}\" exists in the dictionary.")
else:
    print("Key not found in the dictionary")
#!/usr/bin/python3


# Write a Python program to remove a key from a dictionary.

# Write your program below

user = {
    "name" : "John Smith",
    "gender" : "Male",
    "age" : 25,
    "job" : "Engineer",
    "country" : "Nigeria"
    }
print(f"Original dictionary: {user}")
update = user.pop("name")
print(f"Updated dictionary: {user}")
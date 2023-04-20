#!/usr/bin/python3


# Write a Python program to sort a dictionary by key.

# Write your program below

user = {
    "name" : "John Smith",
    "gender" : "Male",
    "age" : 25,
    "job" : "Engineer",
    "country" : "Nigeria"
    }
sort_list = sorted(user.items())    # convert to a list
sort_dict = dict(sort_list)
print(f"Original dictionary: {user}")
print(f"Sorted dictionary: {sort_dict}")
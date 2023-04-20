#!/usr/bin/python3


# Write a Python program to create a dictionary from two lists, one containing keys and the other containing values.

# Write your program below
subjects = ["maths", "eng", "bio", "phy", "chem"]
scores = [50, 45, 78, 90, 67]
my_dict = dict(zip(subjects, scores))  #zip function is used to pair elements in the 2 variables, creating a tuple, then the dict converts them to dictionary

print(my_dict)
#!/usr/bin/python3


# Write a Python program to check whether all values in a dictionary are unique.

# Write your program below
subjects = {
    "mathematics":89, 
    "english":78, 
    "science":50, 
    "Yoruba": 70, 
    "History": 56, 
    "Literature": 87
    }
scores = subjects.values()
unique = set(scores)    #since sets do not accept duplicates, convert to a set and assign to a new variable.

if len(scores) == len(unique):  # if the lengths are the same, it means that all the values are the same.
    print("All the values in the dictionary are unique.")
else:   #if the lengths are different, it means that some of the values are not unique
    print("Some values are identical and are not unique.")



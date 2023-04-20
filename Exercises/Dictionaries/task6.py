#!/usr/bin/python3


# Write a Python program to find the highest and lowest values in a dictionary.

# Write your program below

subjects = {"mathematics":89, "english":78, "science":50}


print(f"Number of coureses taken: {len(subjects)}")

highest = max(subjects.values())
lowest = min(subjects.values())
print(f"The highest score: {highest}")
print(f"The lowest score: {lowest}")
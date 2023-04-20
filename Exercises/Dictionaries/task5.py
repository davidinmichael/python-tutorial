#!/usr/bin/python3

# Write a Python program to find the sum of all items in a dictionary.

# Write your program below

subjects = {"mathematics":89, "english":78, "science":50}


print(f"Number of coureses taken: {len(subjects)}")

sum_of_scores = sum(subjects.values())
print(f"Sum total of all scores: {sum_of_scores}")

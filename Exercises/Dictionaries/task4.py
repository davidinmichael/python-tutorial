#!/usr/bin/python3

# Write a Python program to concatenate two dictionaries.

# Write your program below

core_subjects = {"mathematics":89, "english":78, "science":50}
optional_subjects = {"Yoruba": 70, "History": 56, "Literature": 87}
total = {**core_subjects, **optional_subjects}  
#core_subjects.update(optional_subjects)  #Another method

print(f"Compulsory coureses: {core_subjects}")
print(f"Optional coureses: {optional_subjects}")
print(f"Total results: {total}")


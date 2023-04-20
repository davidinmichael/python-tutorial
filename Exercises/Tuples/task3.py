#!/usr/bin/python3


# Write a program that takes a tuple of strings and returns a new tuple containing only the strings that start with the letter "a".
# Example:
# tup = ("apple", "banana", "avocado", "grape", "apricot")
# Output: ("apple", "avocado", "apricot")

# Write your program below
tup1 = ("apple", "banana", "avocado", "grape", "apricot")
for tup in tup1:
    if tup[0] == "a":
        print(tup)

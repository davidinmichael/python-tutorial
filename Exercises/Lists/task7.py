#!/usr/bin/python3

# Write a Python program to sort a list of numbers in descending order.
# Write your program below

lists = [21, 201, 54, 66, 100, -1000, 43, 200]
print("Original List: {}".format(lists))
lists.sort(reverse=True)
print("Sorted list in descending order: {}".format(lists))

#!/usr/bin/python3

# Write a Python program to find the second largest number in a list.
# Write your program below
lists = [21, 201, 54, 66, 100, -1000, 43, 200]
print(f"List is : {lists}")
lists.sort(reverse=True)
print(f"Sorted List is : {lists}", end=", ")
print(f"and the second largest number is {lists[1]}")

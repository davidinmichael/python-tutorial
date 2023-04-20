#!/usr/bin/python3

# Write a Python program to find the second largest number in a list.
# Write your program below

my_list = [100, 56, 34, 10, 90, 45]
new_list = sorted(my_list, reverse=True)

print(f"The second largest number in the list is {new_list[1]}")

#!/usr/bin/python3

# Write a Python program to remove duplicates from a list.
# Write your program below

num_list = [21, 201, 54, 66, 100, -100, 201, 200, 55, 54, 43, 200]
print("Initial List: {}".format(num_list))

temp = set(num_list)

num_list = list(temp)
print("New List: {}".format(num_list))

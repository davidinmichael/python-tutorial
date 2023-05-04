#!/usr/bin/python3

# Write a Python program to concatenate two lists.
# Write your program below

num_list = [21, 201, 54, 66, 100, -1000, 43, 200]
alpha_list = ["a", "e", "i", "o", "u"]

new_list = num_list + alpha_list

print("Using a new list to concatenate: {}".format(new_list))

num_list.extend(alpha_list)
print("Using the Extend function: {}".format(num_list))

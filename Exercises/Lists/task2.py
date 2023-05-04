#!/usr/bin/python3

# Write a Python program to find the largest number in a list.
# Write your program below

num_list = [21, 201, 54, 66, 100, -1000, 43, 200]

large = num_list[0]
for n in range(1, len(num_list)):
    if num_list[n] > large:
        large = num_list[n]

print(f"The largest number in the list: {num_list} = {large}")

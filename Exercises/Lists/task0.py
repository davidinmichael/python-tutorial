#!/usr/bin/python3

# Write a Python program to reverse a list.
# Write your program below
new_list = []
num_list = [21, 201, 54, 66, 100, -1000, 43, 200]
for i in num_list[::-1]:
    new_list.append(i)
print(new_list)

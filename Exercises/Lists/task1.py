#!/usr/bin/python3

# Write a Python program to find the sum of all the elements in a list.
# Write your program below

num_list = [21, 201, 54, 66, 100, -1000, 43, 200]
total = 0
for n in num_list:
    total += n
print("The sum of elements in {} = {}".format(num_list, total))

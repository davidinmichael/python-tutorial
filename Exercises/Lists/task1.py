#!/usr/bin/python3

# Write a Python program to find the sum of all the elements in a list.
# Write your program below


my_list = [15, 20, 25, 30, 10]
total = 0

for num in my_list:
    total = num + total
print(f"The total of {my_list} is {total}")
#!/usr/bin/python3

# Write a Python program to find the largest number in a list.
# Write your program below

my_list = [75, 20, 2.5, 30, 100]
count = 0

for num in my_list:
    if num > count:
        count = num
print(f"The largest number on the list is: {count}")
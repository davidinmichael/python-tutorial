#!/usr/bin/python3

# Write a Python program to remove duplicates from a list.
# Write your program below

my_list = [100, 50, 78, 100, 98, 50]
new_set = set(my_list)   #Convert to a set. This is because, sets do not accept duplicates and hence are automatically removed.
new_list = list(new_set)   #Convert back to a list.

print(f"The original list is: {my_list}")
print(f"The new list is: {new_list}")
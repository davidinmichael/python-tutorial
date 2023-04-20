#!/usr/bin/python3


# Create two sets with the elements 1, 2, 3, 4, 5 and 4, 5, 6, 7, 8. Find the
# union, intersection,
# and difference of the two sets.

# Write your program below
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"The union of the two sets are: {set1 | set2}")
print(f"The intersection of the two sets are: {set1 & set2}")

#!/usr/bin/python3


# Create two sets with the elements 1, 2, 3 and 2, 3, 4. 
# Find the symmetric difference of the two sets.

# Write your program below
set1 = {1, 2, 3}
set2 = {2, 3, 4}

set3 = set1.symmetric_difference(set2)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"The symetric difference = {set3}")


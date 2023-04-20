#!/usr/bin/python3


# Create a set with the elements 1, 2, 3, 4, 5. Add 6 to the set and then clear the set.

# Write your program below

set1 = {1, 2, 3, 4, 5}
print(f"Original set: {set1}")
set1.add(6)
print(f"6 has been added. New set: {set1}")
set1.clear()
print(f"The set has been cleared. New set = {set1}")
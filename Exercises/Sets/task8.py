#!/usr/bin/python3


# Create a set with the elements apple, banana, cherry, date.  Create a copy of the set and add elderberry to the copy. 
# Check if the original set has been modified.

# Write your program below

set1 = {"apple", "banana", "cherry", "date"}
print(f"Original set: {set1}")

set2 = set1.copy()
print(f"A copy of the set: {set2}")

set2.add("elderberry")

print(f"Original set: {set1}")
print(f"New copied set: {set2}")


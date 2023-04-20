#!/usr/bin/python3


# Create a set with the elements 5, 10, 15, 20, 25. Add 30 to the set and remove 5 from the set.
# Write your program below

set1 = {5, 10, 15, 20, 25}

print(f"The original set: {set1}")
set1.add(30)
set1.discard(5)
print(f"The updated set: {set1}")

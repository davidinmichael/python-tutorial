#!/usr/bin/python3


# Create a set with the elements 1, 2, 3, 4, 5. 
# Remove all even numbers from the set.

# Write your program below

set1 = {1, 2, 3, 4, 5}
set2 = set1.copy()
for num in set2:
    if num % 2 == 0:
        set1.discard(num)

print(set1)
#!/usr/bin/python3


# Create a set with the elements cat, dog, rabbit, hamster. Add dog to the set again and check the length of the set.

# Write your program below

set1 = {"cat", "dog", "rabbit", "hamster"}
print(f"Length of the set: {len(set1)}")
set1.add("dog")
print(f"Length of the set after adding dog again: {len(set1)}")
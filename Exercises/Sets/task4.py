#!/usr/bin/python3


# Create a set with the elements apple, banana, cherry, date. 
# Check if banana is a member of the set
# and remove it from the set.

# Write your program below
set1 = {"apple", "banana", "cherry", "date"}
print(f"The original set: {set1}")
if "banana" in set1:
    print("Banana has been removed.")
    set1.discard("banana")
print(f"The updated set is: {set1}")

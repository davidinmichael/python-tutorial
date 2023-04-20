#!/usr/bin/python3


# Write a program that takes two tuples of integers and returns a new tuple containing the sum of the
# corresponding elements of each tuple.
# Example:
# tup1 = (1, 2, 3)
# tup2 = (4, 5, 6)
# Output: (5, 7, 9)

# Write your program below
tup1 = (10, 20, 30, 40, 50)
tup2 = (60, 70, 80, 90, 100)

print(f"First list: {tup1}")
print(f"Second list: {tup2}")

tup3 = zip(tup1, tup2)  #pairs tup1 and tup2 together
tup4 = []

for tups in tup3:
    tup4.append(sum(tups))  #find the sum of the paired tupules and append to an empty list
print(f"Total: {tuple(tup4)}")  #convert the list back to a tuple and print

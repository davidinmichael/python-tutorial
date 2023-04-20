#!/usr/bin/python3


# Write a program that takes a tuple of tuples and returns a new tuple containing the diagonal elements of the matrix.
# Example:
# tup = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# Output: (1, 5, 9)

# Write your program below

tup1 = ((1, 2, 3), 
        (4, 5, 6), 
        (7, 8, 9))
list1 = []
i = 0
for tup in tup1:
    list1.append(tup[i])
    i = i + 1
print(tuple(list1))
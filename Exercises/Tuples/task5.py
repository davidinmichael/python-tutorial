#!/usr/bin/python3


# Write a program that takes a tuple of integers and returns a new tuple containing only the even numbers.
# Example:
# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Output: (2, 4, 6, 8)

# Write your program below

tup1 = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
list1 = []

for tup in tup1:
    if tup % 2 == 0:
        list1.append(tup)
        tup2 = tuple(list1)
    else:
        continue
print(tup2)

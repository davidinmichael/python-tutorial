#!/usr/bin/python3

# Write a program that defines a function called calculate_distance that takes two sets
# of coordinates (x1, y1) and (x2, y2) as arguments and calculates the Euclidean distance
# between them using the math module. Then, ask the user to input the coordinates of two
# points and print the distance between them.

# Write your program below
from math import sqrt

def euc_distance(pt1=[], pt2=[]):
    if pt1 is None or pt2 is None:
        return
    distance = sqrt((pt2[0] - pt1[0])**2 + (pt2[1] - pt1[1])**2)
    return (distance)

def accept(char):
    data = 0
    while True:
        try:
            data = int(input("Enter Point {}: ".format(char)))
            return (data)
        except:
            print("Numeric data required.")
    return (0)

row1 = []
row2 = []
for i in range(2):
    row1.append(accept("X" + str(i + 1)))
    row2.append(accept("Y" + str(i + 1)))
row1[1], row2[0] = row2[0], row1[1]
distance = euc_distance(row1, row2)
result = """
The Euclidean distance from point {} to point {} is {:.4f}
"""
print(result.format(row1, row2, distance))


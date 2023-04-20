#!/usr/bin/python3
import math

# Write a program that defines a function called calculate_distance that takes two sets
# of coordinates (x1, y1) and (x2, y2) as arguments and calculates the Euclidean distance
# between them using the math module. Then, ask the user to input the coordinates of two
# points and print the distance between them.

# Write your program below

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 
    return(distance)

x1 = float(input("Enter your x1: "))
y1 = float(input("Enter your y1: "))
x2 = float(input("Enter your x2: "))
y2 = float(input("Enter your y2: "))

dist = calculate_distance(x1, y1, x2, y2)
print(f"The Euclidean distance is = {dist:.2f}")

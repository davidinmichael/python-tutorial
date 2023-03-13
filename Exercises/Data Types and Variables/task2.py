#!/usr/bin/python3

# Write a Python program that calculates the area of a rectangle. The program should ask the user to enter
# the length and width of the rectangle, and then print the area.
# Write your program below

length = float(input("Enter Length: "))
width = float(input("Enter Width: "))

area = length * width

print(f"Area of rectangle with width {width} and length {length} is {area}")

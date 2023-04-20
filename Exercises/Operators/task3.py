#!/usr/bin/python3

# Write a Python program that calculates the area of a circle. The program should ask the user to enter
# the radius of the circle, and then print the area. The value of pi can be approximated as 3.14.
# Write your program below

pi = 3.142
radius = int(input("Enter the radius of the circle: "))
area = pi * (radius ** 2)

print(f"The area of the circle is {area:.2f}.")

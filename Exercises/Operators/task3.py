#!/usr/bin/python3
from math import pi as PI

# Write a Python program that calculates the area of a circle. The program should ask the user to enter
# the radius of the circle, and then print the area. The value of pi can be approximated as 3.14.
# Write your program below

radi = 0
area = 0
radi = int(input("Radius: "))
area = PI * (radi ** 2)
print(f"Area of Circle with radius of {radi} = {area:.2f}")

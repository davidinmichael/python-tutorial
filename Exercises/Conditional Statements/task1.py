#!/usr/bin/python3

# Write a program that takes an integer as input and prints whether it is positive, negative, or zero.
# Write your program below

num = int(input("Enter a Number:"))
if num < 0:
    print("Negative number")
elif num == 0:
    print("Zero is the number")
else:
    print("Positive number")

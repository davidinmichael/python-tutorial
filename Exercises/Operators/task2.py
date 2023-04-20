#!/usr/bin/python3
# Write a Python program that checks whether a number entered by the user is even or odd.
# Write your program below



num = int(input("Enter a number: "))

if (num % 2 == 0):
	print(f"{num} is an even number.")
else:
	print(f"{num} is an odd number.")

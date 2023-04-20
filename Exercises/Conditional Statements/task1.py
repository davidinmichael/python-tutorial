#!/usr/bin/python3
# Write a program that takes an integer as input and prints whether it is positive, negative, or zero.
# Write your program below


num = int(input("Enter a number: "))
if (num < 0):
	print(f"{num} is a negative number.")
elif (num == 0):
	print("You have entered zero.")
else:
	print(f"{num} is a positive number.")

#!/usr/bin/python3
# Write a program that takes a number as input and prints whether it is odd or even.
# Write your program below


num = int(input("Enter any number: "))

if (num % 2 == 0):
	print(f"{num} is an even number.")
else:
	print(f"{num} is an odd number.")

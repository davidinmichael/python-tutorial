#!/usr/bin/python3
# Write a program that takes two integers as input and prints the larger one.
# Write your program below


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if (num1 > num2):
	print(num1)
elif (num2 > num1):
	print(num2)
elif (num1 == num2):
	print("Both numbers are equal.")

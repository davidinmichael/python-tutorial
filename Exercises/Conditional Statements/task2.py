#!/usr/bin/python3

# Write a program that takes two integers as input and prints the larger one.
# Write your program below

num1, num2 = input("Enter two numbers: ").split()
num1 = int(num1)
num2 = int(num2)
if num2 > num1:
    print(f"Max of {num1:d} and {num2:d} = {num2:d}")
elif num2 == num1:
    print(f"Both {num1:d} and {num2:d} are equivalent")
else:
    print(f"Max of {num1:d} and {num2:d} = {num1:d}")

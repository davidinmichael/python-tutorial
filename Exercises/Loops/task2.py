#!/usr/bin/python3

# Write a program that asks the user to input a number and then prints the multiplication table for that number up to 10.
# Write your program below

num = int(input("Enter a number: "))
times = 1

while times <= 10:
	ans = num * times
	print(f"{num} x {times} = {ans}")
	times = times + 1

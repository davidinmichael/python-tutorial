#!/usr/bin/python3

# Write a program that prints all the numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number. For multiples of both 3 and 5, print "FizzBuzz" instead of the number.
# Write your program below


num = 1

while (num <= 100):
	if ((num % 3 == 0) and (num % 5 == 0)):
		print("FizzBuzz", end = " ")
	elif (num % 3 == 0):
		print("Fizz", end = " ")
	elif (num % 5 == 0):
		print("Buzz", end = " ")
	else:
		print(num, end = " ")
	num = num + 1
print()

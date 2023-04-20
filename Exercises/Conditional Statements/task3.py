#!/usr/bin/python3
# Write a program that takes a string as input and prints whether it contains the letter "a".
# Write your program below


check_letter = input("Enter your name: ").lower()

for  check in check_letter:
	if check == "a":
		print('Your name contains the letter "a".')
		break
	else:
		print('Your name does not contain the letter "a".')
		break


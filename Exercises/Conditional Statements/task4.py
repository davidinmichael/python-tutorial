#!/usr/bin/python3

# Write a program that takes a year as input and prints whether it is a leap year or not.
# Write your program below

"""
FUN FACT!

Did you know....that, not every year divisible by 4 is a leap year?
The rule is that if the year is divisible by 100 and not divisible by 400, the leap year is skipped. The year 2000 was a leap year for example, but the years 1700, 1800, and 1900 were not. The next time a leap year will be skipped is the year 2100.

You're welcome. :-)

"""

year = int(input("Enter your year of birth: "))
if (year <= 0):
	print("You have entered an invalid year.")
elif (year % 4 == 0):
	if ((year % 100 == 0) and (year % 400 != 0)):
		print(f"{year} is not a leap year.")
	else:
		print(f"{year} is a leap year.")
else:
	print(f"{year} is not a leap year.")



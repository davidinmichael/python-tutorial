#!/usr/bin/python3

# Write a program that takes a year as input and prints whether it is a leap year or not.
# Write your program below
lpyr = input("Enter a year: (4 digits) ")
if len(lpyr) != 4:
    print(f"{leapyear} not a valid year")
lpyr = int(lpyr)
if lpyr % 400 == 0 and lpyr % 100 == 0:
    print(f"{lpyr:d} is a leap year.")
elif lpyr % 4 == 0 and lpyr % 100 != 0:
    print(f"{lpyr:d} is a leap year.")
else:
    print(f"{lpyr:d} is not a leap year.")

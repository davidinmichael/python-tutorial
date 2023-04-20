#!/usr/bin/python3

# Write a program that uses a loop to find the largest number in a list of numbers entered by the user.
# Write your program below

num = input("Enter a series a\of numbers separated by a space: ")
num_list = list(map(float, num.split()))

for no in num_list:
    print(f"The largest number entered is: {max(num_list)}")
    break
#print(num_list)

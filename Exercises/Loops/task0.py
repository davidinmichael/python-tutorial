#!/usr/bin/python3

# Write a program that asks the user to enter a series of numbers and then prints out the number of even and odd numbers entered.
# Write your program below

numbers = input("Enter a series of numbers: ")   #Asks user for input
num_list = map(float, numbers.split())  #splits numbers into individual floats
even_count = 0
odd_count = 0

for no in num_list:
    if no % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"The number of even numbers = {even_count} and odd numbers = {odd_count}.")

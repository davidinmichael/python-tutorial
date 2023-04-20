#!/usr/bin/python3

# Write a Python program to count the number of occurrences of a given element in a list.
# Write your program below

my_list = [1, 1, 1, 2, 3, 4, 4, 4, 4, 5, 5, 6, 7, 7, 8, 8, 8, 8, 9, 10]

num = int(input("Select a whole number from 1 - 10 to check how many times it occurs in the list: \n"))
if num <= 0:
    print("You have entered a number that isn't on the list")
elif num > 0 and num <= 10:
    print(f"The number \"{num}\" appears {my_list.count(num)} time(s)")
else:
    print("You have entered an element that isn't on the list")
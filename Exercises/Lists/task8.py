#!/usr/bin/python3

# Write a Python program to remove the first occurrence of a given element from a list.
# Write your program below

my_list = [1, 1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 9, 10]

print(f"The original list is: {my_list}")
num = int(input("Enter the number you would like to remove: \n"))
if num <= 0:
    print("You have entered a number that isn't on the list")
elif num > 0 and num <= 10:
    my_list.remove(num)
    print(f"The number \"{num}\" has been removed from the list. \nThe new list is: {my_list}")
else:
    print("You have entered an element that isn't on the list")
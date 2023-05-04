#!/usr/bin/python3

# Write a Python program to check if a given element exists in a list.
# Write your program below

lists = [21, 201, 54, 66, 100, -1000, 43, 200, 'a', 'e', 'i', 'o', 'u']
resp = input("Enter a number or character: ")
if resp in lists:
    idx = lists.index(resp, 0, -1)
    print("'{}' was found in the list: {} at index of {}".format(resp, lists, idx))
else:
    print("'{}' was NOT found in the list: {}".format(resp, lists))

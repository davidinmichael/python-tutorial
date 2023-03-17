#!/usr/bin/python3

# Write a Python program to count the number of occurrences of a given element in a list.
# Write your program below
mylist = ["b", "a", "n", "k", "e", "r", "s", "r", "i", "g", "h", "t", "b"]

def get_occurrence(char, lists):
    if lists is None or lists == []:
        return
    count = 0
    for i in lists:
        if char == i:
            count += 1
    if count == 0:
        return 0
    return count


data = input("What character ? ")
result = get_occurrence(data, mylist)
if result is None:
    print("This list is empty")
elif result == 0:
    print(f"\"{data}\" was not found in the list: {mylist}")
else:
    print(f"\"{data}\" was found in the list: {mylist} {result} times.")

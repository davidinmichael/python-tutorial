#!/usr/bin/python3

# Write a program that defines a function called reverse_string that takes a string as an argument and
# returns the reversed string using the reversed function from the builtins module. Then, ask the user
# to input a string and print the reversed string.

# Write your program below

def reverse_string(strchr):
    if strchr == "":
        return
    strchr = "".join(reversed(strchr))
    return (strchr)

myinput = input("Enter a word or sentence: ")
print("Original String:\n{}\n".format(myinput))
print("\nReversed String:\n{}".format(reverse_string(myinput)))

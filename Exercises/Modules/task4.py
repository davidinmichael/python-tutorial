#!/usr/bin/python3
import builtins

# Write a program that defines a function called reverse_string that takes a string as an argument and returns the reversed string using the reversed function
# from the builtins module. Then, ask the user
# to input a string and print the reversed string.

# Write your program below

def rev_str(str):
    str = input("Enter your name: ").lower()
    rev = list(reversed(str))  #convert to a list  and reverse the list
    new_str = ''.join(rev)  #convert the list back to a string
    return(new_str)
x = rev_str(str)
print(f"The reverse spelling of your name is: \"{x}\"")
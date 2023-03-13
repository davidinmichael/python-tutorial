#!/usr/bin/python3

# Write a Python program that calculates the sum and product of two numbers entered by the user.
# Write your program below

first, second = input(" Enter two numbers: ").split()
first = int(first)
second = int(second)
summ = first + second
prod = first * second
print("{0} and {1}. " \
      "Their sum is {2} and their product" \
      " is {3}".format(first, second, summ, prod))


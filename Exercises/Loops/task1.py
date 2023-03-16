#!/usr/bin/python3

# Write a program that prints all the numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number. For multiples of both 3 and 5, print "FizzBuzz" instead of the number.
# Write your program below
for i in range(1, 101):
    if i == 100:
        print("{}".format(i), end="")
        break
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print("{}".format(i), end=" ")

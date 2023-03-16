#!/usr/bin/python3

# Write a program that uses a loop to print out the first 10 Fibonacci numbers.
# Write your program below

first_val = 0
second_val = 1
for i in range(11):
    if i <= 1:
        fib = i
    else:
        fib = first_val + second_val
        # first_val = second_val
        # second_val = fib
        first_val, second_val = second_val, fib
print(fib)
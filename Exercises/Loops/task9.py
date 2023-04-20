#!/usr/bin/python3

# Write a program that uses a loop to print out the first 10 Fibonacci numbers.
# Write your program below

#formula = fn = fn-1 + fn-2
# 0 1 1 2 3 5 8 13 21 34

num1 = 0
num2 = 1

print(num1, num2, sep=" ", end=" ")
for nums in range(8):
    num3 = num2 + num1

    print(num3, end=" ")

    num1 = num2
    num2 = num3
print()
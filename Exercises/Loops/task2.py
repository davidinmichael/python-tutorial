#!/usr/bin/ptyhon3

# Write a program that asks the user to input a number and then prints the multiplication table for that number up to 10.
# Write your program below
num = 0
while True:
    try:
        num = int(input("Enter a Number: "))
        break
    except ValueError:
        print("Numeric data required.")

for i in range(1, (num + 1)):
    print(f"=== {i} Times Table ===")
    for j in range(1, 11):
        print("{:d} * {:d} = {:d}".format(i, j, (i * j)))
    print()

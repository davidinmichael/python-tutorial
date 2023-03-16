#!/usr/bin/python3

# Write a program that asks the user to enter a series of numbers and then prints out the number of even and odd numbers entered.
# Write your program below

def acceptval(strchr):
    while True:
        try:
            num = int(input(f"Enter {strchr}: "))
            return (num)
        except:
            print("Numeric value required.")

num = []
rng = acceptval("Range")
for i in range(rng):
    num.append(acceptval("Number"))
for n in num:
    print("{} is {}".format(n, ("Even" if n % 2 == 0 else "Odd")))


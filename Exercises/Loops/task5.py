#!/usr/bin/python3

# Write a program that uses a loop to find the largest number in a list of numbers entered by the user.
# Write your program below
def accept_val(strchr):
    while True:
        try:
            numbe = int(input("Enter {}: ".format(strchr)))
            return numbe
        except ValueError:
            print("Please provide a numeric data")


numb = []
res = 'y'
while True:
    numb.append(accept_val("Number"))
    res = input("More numbers (y/n)? ")
    if res not in 'Yy':
        break
largest = numb[0]
for i in range(1, len(numb)):
    if largest < numb[i]:
        largest = numb[i]
print("The largest value in {} is {}".format(numb, largest))

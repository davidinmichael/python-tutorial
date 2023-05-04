#!/usr/bin/python3

# Write a program that asks the user to enter a series of words and then prints out the words in alphabetical order.
# Write your program below
strlist = []
res = 'y'
while True:
    strlist.append(input("Word: "))
    res = input("More words (y/n)? ")
    if res not in 'Yy':
        break
strlist.sort()
for st in strlist:
    print(st)

# Write a program that takes a year as input and prints whether it is a leap year or not.
# Write your program below
y = int(input("Enter a year: "))
if (y % 4 == 0):
    print("It's a Leap Year")
elif (y % 400 == 0):
    print("It is a Leap Year")
else:
    print("It is not a Leap Year")

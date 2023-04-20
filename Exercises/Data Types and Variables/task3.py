#!/usr/bin/python3

# Write a Python program that converts Fahrenheit temperatures to Celsius temperatures.
# The program should ask the user to enter a temperature in Fahrenheit,and then print the
# equivalent temperature in Celsius.The conversion formula is: C = (F - 32) * 5/9
# write your program below

f_temp = int(input("Enter the temperature in Fahrenheiht: "))
c_temp = ((f_temp - 32) * (5/9))

print(f"{f_temp}F to Celsius = {c_temp:.2f}⁰C")
